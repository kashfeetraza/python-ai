"""Pricing helpers for Sweet Crumbs."""

DELIVERY_FEE = 200
FREE_DELIVERY_FROM = 3000


def delivery_fee(subtotal: int) -> int:
    """Return the delivery fee in PKR."""
    if subtotal >= FREE_DELIVERY_FROM:
        return 0
    return DELIVERY_FEE


def order_total(price: int, quantity: int) -> int:
    """Return item subtotal plus delivery."""
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity cannot be negative.")
    subtotal = price * quantity
    return subtotal + delivery_fee(subtotal)


if __name__ == "__main__":
    assert delivery_fee(1000) == 200
    assert delivery_fee(3000) == 0
    assert order_total(250, 4) == 1200
    print("pricing.py: all tests passed")
