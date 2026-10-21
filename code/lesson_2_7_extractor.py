
"""Lesson 2.7: Extract, validate, calculate, and save bakery orders."""

import json

import httpx
import ollama
from langchain.chat_models import init_chat_model

PRICES = {
    "chocolate cake": 1500,
    "cupcake": 250,
    "brownie": 300,
}

ORDER_SCHEMA = {
    "type": "object",
    "properties": {
        "customer": {"type": "string"},
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "quantity": {"type": "integer"},
                },
                "required": ["name", "quantity"],
            },
        },
        "address": {"type": "string"},
    },
    "required": ["customer", "items", "address"],
}

SYSTEM = (
    "Extract a bakery order from the customer's message. "
    f"Allowed menu items: {', '.join(PRICES)}. "
    "Extract only details supported by the message. "
    "If customer name or address is missing, use an empty string. "
    "If the message is not an order, return an empty items list. "
    "Do not invent details. "
    "Quantities must be whole numbers. "
    "Normalize item names to the closest exact menu name only "
    "when the message clearly identifies that item. "
    "If an item is ambiguous, preserve its name so it can be checked."
)

extractor = init_chat_model(
    "llama3.2",
    model_provider="ollama",
    temperature=0,
    format=ORDER_SCHEMA,
)


def validate_order(order: dict, message: str) -> list[str]:
    """Check extracted fields against the message and trusted menu."""
    problems = []

    if not isinstance(order, dict):
        return ["AI response is not a JSON object"]

    if not isinstance(order.get("customer"), str):
        return ["Customer name must be text"]

    if not isinstance(order.get("address"), str):
        return ["Address must be text"]

    if not isinstance(order.get("items"), list):
        return ["Items must be a list"]

    customer = order["customer"]
    address = order["address"]

    if customer and customer.casefold() not in message.casefold():
        problems.append(
            f"Customer '{customer}' is not found in the original message"
        )

    if address and address.casefold() not in message.casefold():
        problems.append(
            f"Address '{address}' is not found in the original message"
        )

    for index, item in enumerate(order["items"], start=1):
        if not isinstance(item, dict):
            problems.append(f"Item {index} is not an object")
            continue

        name = item.get("name")
        quantity = item.get("quantity")

        if not isinstance(name, str) or not name.strip():
            problems.append(f"Item {index} has an invalid name")
            continue

        if name.casefold() not in PRICES:
            problems.append(f"'{name}' is not on the menu")

        # bool is a subclass of int in Python, so exclude it explicitly.
        if (
            not isinstance(quantity, int)
            or isinstance(quantity, bool)
            or quantity <= 0
        ):
            problems.append(
                f"Quantity for '{name}' must be a positive whole number"
            )

    return problems


def process_message(message: str) -> dict | None:
    """Extract an order, validate it, and calculate its total in Python."""
    try:
        response = extractor.invoke(
            [
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": message},
            ]
        )
        order = json.loads(response.text)

    except json.JSONDecodeError:
        print("Could not read the AI reply as JSON.")
        return None
    except httpx.ConnectError:
        print("Ollama is offline. Start Ollama and try again.")
        return None
    except ollama.ResponseError as error:
        print(f"Ollama model error: {error}")
        return None
    except (TypeError, ValueError) as error:
        print(f"Could not process this message: {error}")
        return None

    if not isinstance(order, dict):
        print("AI returned an unexpected data structure.")
        return None

    items = order.get("items")

    if not isinstance(items, list):
        print("AI response has an invalid items field.")
        return None

    print(f"\nMessage: {message}")

    if len(items) == 0:
        print("Not an order: needs a human reply.")
        return None

    problems = validate_order(order, message)
    total = 0

    for item in items:
        if not isinstance(item, dict):
            continue

        name = item.get("name")
        quantity = item.get("quantity")

        if not isinstance(name, str):
            continue

        name = name.casefold()

        if name not in PRICES:
            continue

        if (
            not isinstance(quantity, int)
            or isinstance(quantity, bool)
            or quantity <= 0
        ):
            continue

        line_total = PRICES[name] * quantity
        total += line_total
        print(f"  {quantity} x {name} = {line_total} PKR")

    order["total"] = total
    order["problems"] = problems
    order["source_message"] = message

    customer = order.get("customer", "")
    address = order.get("address", "")

    print(f"  Customer: {customer or '(missing)'}")
    print(f"  Address: {address or '(missing)'}")
    print(f"  Total of recognized valid items: {total} PKR")

    for problem in problems:
        print(f"  CHECK: {problem}")

    if problems:
        print("  Status: REVIEW REQUIRED")
    else:
        print("  Status: Checks passed")

    return order


def main() -> None:
    """Process sample WhatsApp messages and save extracted orders."""
    messages_in = [
        "Salam! 2 cupcakes aur 1 chocolate cake chahiye. "
        "Ali, house 12 Gulberg",
        "3 brownies please, Sara, DHA phase 5",
        "hi do you deliver to Johar Town?",
        "1 pizza and 2 brownies",
        "same as last time please",
        "I want five brownies",
    ]

    saved = []

    for message in messages_in:
        order = process_message(message)

        if order is not None:
            saved.append(order)

    try:
        with open("orders.json", "w", encoding="utf-8") as file:
            json.dump(
                saved,
                file,
                indent=2,
                ensure_ascii=False,
            )

        print(f"\nSaved {len(saved)} orders to orders.json")

    except OSError as error:
        print(f"Could not save orders.json: {error}")


if __name__ == "__main__":
    main()
