
"""Lesson 3.3: Get today's USD exchange rate."""

import httpx

URL = "https://open.er-api.com/v6/latest/USD"


def main():
    try:
        response = httpx.get(URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("result") != "success":
            print("Exchange rate API returned an error.")
            return

        print("Status:", response.status_code)
        print("Base currency:", data["base_code"])
        print("1 USD =", data["rates"]["PKR"], "PKR")
        print("Last updated:", data["time_last_update_utc"])

    except httpx.HTTPError as error:
        print("API request failed:", error)
    except (ValueError, KeyError) as error:
        print("Unexpected API response:", error)


if __name__ == "__main__":
    main()
