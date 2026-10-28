
"""Load and save Sweet Crumbs business data without replacing existing orders."""

import json
from typing import Any

from sweet_crumbs.config import DATA_FILE

if not DATA_FILE.exists():
    raise SystemExit(
        f"Missing {DATA_FILE}. Keep your existing business.json in the code folder."
    )

try:
    with DATA_FILE.open("r", encoding="utf-8") as file:
        business: dict[str, Any] = json.load(file)
except json.JSONDecodeError as exc:
    raise SystemExit(f"business.json is not valid JSON: {exc}") from exc

if not isinstance(business.get("prices"), dict):
    raise SystemExit('business.json must contain a "prices" dictionary.')
if not isinstance(business.get("orders"), dict):
    # Do not silently invent or overwrite orders.
    raise SystemExit('business.json must contain an "orders" dictionary.')

PRICES: dict[str, int] = business["prices"]
ORDERS: dict[str, str] = business["orders"]


def save() -> None:
    """Persist current business data and orders to business.json."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(business, file, indent=2, ensure_ascii=False)
        file.write("\n")
