"""Extract WhatsApp-style bakery messages into validated Order objects.

Run from the code folder:
    uv run lesson_3_2_order_models.py

This script writes to orders_lesson_3_2.json so it does not overwrite
an existing orders.json file.
"""

import json
from pathlib import Path

from langchain.chat_models import init_chat_model
from langchain_core.exceptions import OutputParserException
from pydantic import ValidationError

from sweet_crumbs.config import MODEL, PROVIDER
from sweet_crumbs.data import PRICES
from sweet_crumbs.models import Order

llm = init_chat_model(MODEL, model_provider=PROVIDER, temperature=0)
extractor = llm.with_structured_output(Order)

SYSTEM = (
    "Extract a bakery order from the customer's message. "
    f"Menu items and prices are: {', '.join(PRICES)}. "
    "Never invent a customer name, item, quantity, phone number, or address. "
    "If the message is not an order, return an empty items list. "
    "Keep item names as menu names when possible."
)

MESSAGES_IN = [
    "Salam! 2 cupcakes aur 1 chocolate cake chahiye. Ali, house 12 Gulberg",
    "1 pizza and 2 brownies please, Model Town",
    "hi do you deliver to Johar Town?",
    "2 brownies please. Sara, Johar Town",
]


def main() -> None:
    saved: list[dict] = []
    for message in MESSAGES_IN:
        print(f"\nMessage: {message}")
        try:
            order = extractor.invoke(
                [
                    {"role": "system", "content": SYSTEM},
                    {"role": "user", "content": message},
                ]
            )
        except (OutputParserException, ValidationError, ValueError) as exc:
            print(f"  CHECK: AI output could not be validated: {exc}")
            print("  Please review this message manually.")
            continue
        except Exception as exc:
            print(f"  CHECK: Model/provider error: {exc}")
            print("  Check that Ollama is running and your configured model is available.")
            continue

        if not order.items:
            print("  Not an order: a human should reply to the customer.")
            continue

        for item in order.items:
            print(f"  {item.quantity} x {item.name}")

        print(f"  Customer: {order.customer or '(missing)'}")
        print(f"  Address: {order.address or '(missing)'}")
        print(f"  Total: {order.total(PRICES):,} PKR")

        problems = order.problems(PRICES, message)
        for problem in problems:
            print(f"  CHECK: {problem}")

        row = order.model_dump()
        row["total"] = order.total(PRICES)
        row["needs_human_review"] = bool(problems)
        row["source_message"] = message
        saved.append(row)

    # Separate output file preserves any existing orders.json.
    output_path = Path("orders_lesson_3_2.json")
    output_path.write_text(
        json.dumps(saved, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\nSaved {len(saved)} extracted orders to {output_path}")


if __name__ == "__main__":
    main()
