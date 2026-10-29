
"""Live currency and weather tools for Sweet Crumbs."""

from langchain.tools import tool
from pydantic import BaseModel, Field, ValidationError

from sweet_crumbs.config import (
    GEOCODE_URL,
    RATES_URL,
    WEATHER_URL,
)
from sweet_crumbs.web import ApiError, get_json


class RatesReply(BaseModel):
    """Validate the exchange-rate response."""

    result: str = Field(description="API result status")
    base_code: str = Field(description="Base currency code")
    time_last_update_utc: str = Field(
        description="Last update time in UTC"
    )
    rates: dict[str, float] = Field(
        description="Exchange rates indexed by currency code"
    )


def describe_weather(code: int) -> str:
    """Convert a WMO weather code into plain language."""

    if code == 0:
        return "clear sky"
    if code in (1, 2, 3):
        return "mainly clear to overcast"
    if code in (45, 48):
        return "fog"
    if 51 <= code <= 67 or 80 <= code <= 82:
        return "rain or drizzle"
    if 71 <= code <= 77 or code in (85, 86):
        return "snow"
    if code >= 95:
        return "thunderstorm"
    return "other conditions"


@tool
def convert_currency(
    amount: float,
    from_currency: str,
    to_currency: str,
) -> str:
    """Convert money using the latest available exchange rate.

    Args:
        amount: Non-negative amount of money to convert.
        from_currency: Three-letter source code, such as PKR.
        to_currency: Three-letter target code, such as USD or AED.
    """
    if amount < 0:
        return "Amount cannot be negative."

    source = from_currency.strip().upper()
    target = to_currency.strip().upper()

    if len(source) != 3 or len(target) != 3:
        return "Use three-letter currency codes such as PKR, USD or AED."

    try:
        raw = get_json(f"{RATES_URL}/{source}")
        reply = RatesReply.model_validate(raw)

        if reply.result != "success":
            return "Exchange rate service returned an error."

        if target not in reply.rates:
            return f"Currency {target} is not available."

        rate = reply.rates[target]
        converted = amount * rate

        return (
            f"{amount:,.2f} {source} = {converted:,.2f} {target}. "
            f"Rate: {rate:g}. Updated: "
            f"{reply.time_last_update_utc}. "
            "Rates by Exchange Rate API."
        )

    except (ApiError, ValidationError, ValueError) as error:
        return f"Currency conversion is unavailable: {error}"


@tool
def get_weather(city: str) -> str:
    """Get current weather for a city to help plan deliveries.

    Args:
        city: City name, for example Lahore or Karachi.
    """
    try:
        places = get_json(
            GEOCODE_URL,
            {"name": city, "count": 1},
        )

        results = places.get("results") or []
        if not results:
            return f"I could not find the city {city}."

        place = results[0]

        forecast = get_json(
            WEATHER_URL,
            {
                "latitude": place["latitude"],
                "longitude": place["longitude"],
                "current": (
                    "temperature_2m,wind_speed_10m,weather_code"
                ),
            },
        )

        current = forecast["current"]
        units = forecast["current_units"]

        condition = describe_weather(
            int(current["weather_code"])
        )

        return (
            f"{place['name']}, {place.get('country', '')}: "
            f"{current['temperature_2m']}"
            f"{units['temperature_2m']}, {condition}, "
            f"wind {current['wind_speed_10m']} "
            f"{units['wind_speed_10m']}."
        )

    except (ApiError, KeyError, TypeError, ValueError) as error:
        return f"Weather is unavailable right now: {error}"


if __name__ == "__main__":
    assert describe_weather(0) == "clear sky"
    assert describe_weather(63) == "rain or drizzle"
    assert describe_weather(95) == "thunderstorm"

    print("live_tools.py: local tests passed")
    print(convert_currency.invoke({
        "amount": 1500,
        "from_currency": "PKR",
        "to_currency": "USD",
    }))
    print(get_weather.invoke({"city": "Lahore"}))
