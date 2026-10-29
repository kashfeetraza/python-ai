"""Small validation demo for Lesson 3.2."""

from pydantic import BaseModel, Field, ValidationError


class DemoOrderItem(BaseModel):
    name: str = Field(min_length=1, description="Name of the menu item")
    quantity: int = Field(gt=0, description="Quantity must be at least 1")


if __name__ == "__main__":
    item = DemoOrderItem(name="cupcake", quantity="3")
    print(item)
    print(item.quantity + 1)
    print(item.model_dump())

    examples = [
        {"name": "brownie", "quantity": 0},
        {"name": "brownie", "quantity": "five"},
        {"quantity": 2},
    ]
    for data in examples:
        try:
            DemoOrderItem(**data)
        except ValidationError as exc:
            print(f"Rejected {data}: {exc.errors()[0]['msg']}")
