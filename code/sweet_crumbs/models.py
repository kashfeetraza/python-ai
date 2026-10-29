"""Validated data models for Sweet Crumbs bakery orders."""

from pydantic import BaseModel, ConfigDict, Field


class OrderItem(BaseModel):
    """One menu item in a customer's order."""

    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(
        min_length=1,
        max_length=80,
        description="Menu item name exactly as mentioned by the customer.",
    )
    quantity: int = Field(
        gt=0,
        le=100,
        description="Number of units requested; must be a whole number from 1 to 100.",
    )


class Order(BaseModel):
    """An order extracted from a customer message."""

    model_config = ConfigDict(str_strip_whitespace=True)

    customer: str = Field(
        default="",
        max_length=100,
        description="Customer name only if stated in the message; otherwise an empty string.",
    )
    items: list[OrderItem] = Field(
        description="Items requested. Use an empty list when the message is not an order.",
    )
    address: str = Field(
        default="",
        max_length=250,
        description="Delivery address only if stated in the message; otherwise an empty string.",
    )

    def total(self, prices: dict[str, int]) -> int:
        """Calculate the total for recognized menu items only, in PKR."""
        total_amount = 0
        for item in self.items:
            name = item.name.casefold()
            if name in prices:
                total_amount += prices[name] * item.quantity
        return total_amount

    def problems(self, prices: dict[str, int], message: str) -> list[str]:
        """Return business-rule issues that need human review."""
        found: list[str] = []
        message_lower = message.casefold()

        for item in self.items:
            if item.name.casefold() not in prices:
                found.append(f"'{item.name}' is not on the menu")

        if not self.customer:
            found.append("customer name is missing")
        elif self.customer.casefold() not in message_lower:
            found.append(f"customer '{self.customer}' is not in the message (possibly invented)")

        if not self.items:
            found.append("no order items were found")

        return found


if __name__ == "__main__":
    test_order = Order(
        customer="Ali",
        items=[
            OrderItem(name="Cupcake", quantity=2),
            OrderItem(name="pizza", quantity=1),
        ],
        address="",
    )
    prices = {"cupcake": 250, "chocolate cake": 1500, "brownie": 300, "donut": 200}

    assert test_order.total(prices) == 500
    assert test_order.problems(prices, "2 cupcakes and a pizza, Ali") == [
        "'pizza' is not on the menu"
    ]
    assert Order(customer="", items=[], address="").problems(prices, "hello") == [
        "customer name is missing",
        "no order items were found",
    ]
    print("models.py: all tests passed")
