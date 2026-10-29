
"""Lesson 3.3: Retry temporary failures only."""

import time

import httpx

URL = "https://open.er-api.com/v6/latest/USD"
RETRY_STATUSES = {429, 500, 502, 503, 504}


def main():
    for attempt in range(1, 4):
        try:
            response = httpx.get(URL, timeout=10)

            if response.status_code in RETRY_STATUSES:
                print(f"Attempt {attempt}: HTTP {response.status_code}")
            else:
                response.raise_for_status()
                data = response.json()

                if data.get("result") != "success":
                    print("The API returned an application error.")
                    return

                print("1 USD =", data["rates"]["PKR"], "PKR")
                return

        except httpx.TimeoutException:
            print(f"Attempt {attempt}: timed out")

        except httpx.TransportError:
            print(f"Attempt {attempt}: network error")

        except httpx.HTTPStatusError as error:
            print(
                "Permanent HTTP error:",
                error.response.status_code,
            )
            return

        if attempt < 3:
            time.sleep(2 ** attempt)

    print("The rate is unavailable after three attempts.")


if __name__ == "__main__":
    main()
