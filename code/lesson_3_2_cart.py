"""Lesson 3.2: a plain class with independent shopping carts."""

class Cart:
    """A customer's shopping cart."""

    def __init__(self, customer: str):
        self.customer = customer
        self.items: dict[str, int] = {}

    def add(self, item: str, quantity: int = 1) -> None:
        """Add a positive quantity of an item to the cart."""
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity < 1:
            raise ValueError("Quantity must be a whole number greater than 0.")
        item = item.strip().lower()
        if not item:
            raise ValueError("Item name cannot be empty.")
        self.items[item] = self.items.get(item, 0) + quantity

    def total(self, prices: dict[str, int]) -> int:
        """Return the total in PKR using the provided price list."""
        total = 0
        for item, quantity in self.items.items():
            if item not in prices:
                raise ValueError(f"'{item}' is not on the menu.")
            total += prices[item] * quantity
        return total


PRICES = {"chocolate cake": 1500, "cupcake": 250, "brownie": 300, "donut": 200}

if __name__ == "__main__":
    ali = Cart("Ali")
    ali.add("cupcake", 2)
    ali.add("cupcake")
    sara = Cart("Sara")
    sara.add("chocolate cake")

    assert ali.items == {"cupcake": 3}
    assert ali.total(PRICES) == 750
    assert sara.total(PRICES) == 1500
    assert type(ali).__name__ == "Cart"
    print(ali.customer, ali.items, ali.total(PRICES))
    print(sara.customer, sara.items, sara.total(PRICES))
    print("lesson_3_2_cart.py: all tests passed")
