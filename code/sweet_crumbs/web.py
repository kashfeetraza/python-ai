
"""Reusable HTTP JSON helper for Sweet Crumbs."""

import time

import httpx

from sweet_crumbs.config import CACHE_SECONDS, HTTP_TIMEOUT

RETRY_STATUSES = {429, 500, 502, 503, 504}
_cache = {}


class ApiError(Exception):
    """An API request failed in a way the application can handle."""


def get_json(
    url: str,
    params: dict | None = None,
    attempts: int = 3,
) -> dict:
    """Fetch JSON with caching, timeout and safe retries."""

    if attempts < 1:
        raise ValueError("attempts must be at least 1")

    cache_key = (url, tuple(sorted((params or {}).items())))
    cached = _cache.get(cache_key)

    if cached and time.time() - cached[0] < CACHE_SECONDS:
        return cached[1]

    last_problem = "Unknown API error"

    for attempt in range(1, attempts + 1):
        try:
            response = httpx.get(
                url,
                params=params,
                timeout=HTTP_TIMEOUT,
            )

            if response.status_code in RETRY_STATUSES:
                last_problem = f"Temporary HTTP {response.status_code}"

                if response.status_code == 429:
                    retry_after = response.headers.get("Retry-After")
                    try:
                        wait = min(float(retry_after), 30) if retry_after else 2 ** (attempt - 1)
                    except ValueError:
                        wait = 2 ** (attempt - 1)
                else:
                    wait = 2 ** (attempt - 1)

                if attempt < attempts:
                    time.sleep(wait)
                    continue

                break

            # Permanent client errors are not retried.
            if response.status_code >= 400:
                raise ApiError(
                    f"API rejected the request: HTTP {response.status_code}"
                )

            try:
                data = response.json()
            except ValueError as error:
                raise ApiError("API did not return valid JSON") from error

            if not isinstance(data, dict):
                raise ApiError("Expected a JSON object from the API")

            _cache[cache_key] = (time.time(), data)
            return data

        except httpx.TimeoutException:
            last_problem = "API request timed out"
        except httpx.TransportError:
            last_problem = "Could not connect to the API"

        if attempt < attempts:
            time.sleep(2 ** (attempt - 1))

    raise ApiError(f"{last_problem}; tried {attempts} times")
