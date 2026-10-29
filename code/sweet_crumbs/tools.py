"""Agent tools for menu prices, order status and owner-approved orders."""

from langchain.tools import tool
from sweet_crumbs.live_tools import convert_currency, get_weather
from sweet_crumbs.data import ORDERS, PRICES, business, save


@tool
def get_price(item: str) -> str:
    """Get the price of one bakery item.

    Args:
        item: The menu item name, for example "cupcake".
    """
    name = item.lower().strip()
    if name in PRICES:
        return f"{name} costs {PRICES[name]} PKR."
    return f"{item} is not on the menu. Available items: {', '.join(PRICES)}."


@tool
def get_business_info() -> str:
    """Get basic business information such as name, city and opening hours."""
    name = business.get("name", "Sweet Crumbs")
    city = business.get("city", "not specified")
    hours = business.get("hours", "not specified")
    delivery = business.get("delivery", "not specified")
    return f"{name} is in {city}. Hours: {hours}. Delivery: {delivery}."


@tool
def order_status(order_id: str) -> str:
    """Check the delivery status of an existing order.

    Args:
        order_id: The order number, for example "A101".
    """
    key = order_id.upper().strip()
    if key not in ORDERS:
        return f"Order {key} was not found."
    return f"Order {key} is {ORDERS[key]}."


@tool
def place_order(item: str, quantity: int, customer: str) -> str:
    """Place a new order only after the owner explicitly approves it.

    Args:
        item: Menu item name, for example "cupcake".
        quantity: Positive number of items to order.
        customer: Customer's name.
    """
    name = item.lower().strip()
    if name not in PRICES:
        return f"{item} is not on the menu. Available items: {', '.join(PRICES)}."
    if quantity <= 0:
        return "Quantity must be a positive whole number."
    if not customer.strip():
        return "A customer name is required."

    total = int(PRICES[name]) * quantity
    approval = input(
        f"  [OWNER APPROVAL] {quantity} x {name} for {customer.strip()} "
        f"= {total} PKR. Place this order? (yes/no): "
    ).strip().lower()
    if approval != "yes":
        return "Order was not placed because the owner did not approve it."

    prefix = str(business.get("order_prefix", "A"))
    next_number = int(business.get("next_order_number", 101))
    order_id = f"{prefix}{next_number}"
    while order_id in ORDERS:
        next_number += 1
        order_id = f"{prefix}{next_number}"

    ORDERS[order_id] = "received"
    business["next_order_number"] = next_number + 1
    save()
    return f"Order {order_id} placed: {quantity} x {name}, total {total} PKR."


TOOLS = {
    "get_price": get_price,
    "get_business_info": get_business_info,
    "order_status": order_status,
    "place_order": place_order,
}

TOOLS.update({
    "convert_currency": convert_currency,
    "get_weather": get_weather,
})
