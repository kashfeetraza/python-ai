
"""Lesson 3.3: Handle errors from external web APIs."""

import httpx


def main() -> None:
    url = "https://open.er-api.com/v6/latest/XYZ"

    try:
        response = httpx.get(url, timeout=10)

        print("Status:", response.status_code)

        response.raise_for_status()
        data = response.json()

        # Validate the API response before accessing its keys.
        if data.get("result") != "success":
            error_message = data.get("error-type", "Unknown API error")
            print(f"API returned an error: {error_message}")
            return

        rates = data.get("rates")

        if not isinstance(rates, dict):
            print("API response does not contain a valid rates object.")
            return

        if "PKR" not in rates:
            print("PKR exchange rate is missing from the response.")
            return

        print("1 XYZ =", rates["PKR"], "PKR")

    except httpx.TimeoutException:
        print("The API request timed out.")

    except httpx.HTTPStatusError as error:
        print(f"HTTP status error: {error.response.status_code}")

    except httpx.RequestError as error:
        print(f"Network request failed: {error}")

    except ValueError:
        print("The API did not return valid JSON.")


if __name__ == "__main__":
    main()
