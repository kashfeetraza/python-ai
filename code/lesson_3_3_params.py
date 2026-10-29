
"""Lesson 3.3: Get current weather with query parameters."""

import httpx

URL = "https://api.open-meteo.com/v1/forecast"

PARAMS = {
    "latitude": 31.558,
    "longitude": 74.3507,
    "current": "temperature_2m,wind_speed_10m",
}


def main():
    try:
        response = httpx.get(URL, params=PARAMS, timeout=10)
        print("Request URL:", response.url)
        response.raise_for_status()

        data = response.json()
        current = data["current"]
        units = data["current_units"]

        print(
            f"Lahore: {current['temperature_2m']} "
            f"{units['temperature_2m']}"
        )
        print(
            f"Wind: {current['wind_speed_10m']} "
            f"{units['wind_speed_10m']}"
        )

    except httpx.HTTPError as error:
        print("Weather request failed:", error)
    except (ValueError, KeyError) as error:
        print("Unexpected weather response:", error)


if __name__ == "__main__":
    main()
