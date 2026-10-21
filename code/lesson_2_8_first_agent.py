
"""Lesson 2.8: Your First Agent — Sweet Crumbs Bakery."""

import json

from langchain.chat_models import init_chat_model
from langchain.tools import tool
from pydantic import ValidationError

MAX_STEPS = 5

PRICES = {
    "chocolate cake": 1500,
    "cupcake": 250,
    "brownie": 300,
}

ORDERS = {
    "A101": "baking",
    "A102": "out for delivery",
    "A103": "delivered",
}


# TOOL 1: Read bakery prices
@tool(parse_docstring=True)
def get_price(item: str) -> str:
    """Get the price of one bakery item.

    Args:
        item: The item name, for example "cupcake".
    """
    name = item.lower().strip()

    if name in PRICES:
        return f"{name} costs {PRICES[name]} PKR"

    return (
        f"{item} is not on the menu. "
        f"Available items: {', '.join(PRICES)}"
    )


# TOOL 2: Check an existing order
@tool(parse_docstring=True)
def order_status(order_id: str) -> str:
    """Check the delivery status of an existing order.

    Args:
        order_id: The order number, for example "A101".
    """
    key = order_id.upper().strip()

    if key not in ORDERS:
        return f"Order {key} was not found."

    return f"Order {key} is {ORDERS[key]}."


# TOOL 3: Place a new order with human approval
@tool(parse_docstring=True)
def place_order(item: str, quantity: int, customer: str) -> str:
    """Prepare a bakery order and ask for owner approval before saving.

    Args:
        item: The bakery item, for example "brownie".
        quantity: The number of items to order, for example 2.
        customer: The customer's name.
    """
    name = item.lower().strip()
    customer = customer.strip()

    # Validate the tool's inputs.
    if name not in PRICES:
        return f"{item} is not on the menu."

    if isinstance(quantity, bool) or not isinstance(quantity, int):
        return "Quantity must be a whole number."

    if quantity < 1 or quantity > 100:
        return "Quantity must be between 1 and 100."

    if not customer:
        return "Customer name is required."

    # Python calculates the total; the AI does not set the price.
    total = PRICES[name] * quantity

    # Require approval before performing the action.
    answer = input(
        f"\n[APPROVAL] {customer}: {quantity} x {name} "
        f"= {total} PKR. Place this order? (yes/no): "
    )

    if answer.strip().lower() != "yes":
        return "Order cancelled. The owner did not approve it."

    # Assign the next ID.
    order_id = f"A{101 + len(ORDERS)}"

    order_data = {
        "id": order_id,
        "item": name,
        "quantity": quantity,
        "customer": customer,
        "total": total,
        "status": "received",
    }

    # Save the approved order as one JSON object per line.
    with open("agent_orders.json", "a", encoding="utf-8") as file:
        file.write(json.dumps(order_data, ensure_ascii=False) + "\n")

    ORDERS[order_id] = "received"

    return (
        f"Order {order_id} placed successfully: "
        f"{quantity} x {name}, total {total} PKR."
    )


# Register tools so the model can select among them.
TOOLS = {
    "get_price": get_price,
    "order_status": order_status,
    "place_order": place_order,
}

llm = init_chat_model(
    "llama3.2",
    model_provider="ollama",
    temperature=0,
)

llm_with_tools = llm.bind_tools(list(TOOLS.values()))

# Memory: keep the conversation messages between turns.
messages = [
    {
        "role": "system",
        "content": (
            "You are the Sweet Crumbs bakery agent. "
            "Use get_price for menu prices and order_status for existing orders. "
            "Use place_order only when the customer clearly asks to order. "
            "Never invent prices, order statuses, or order IDs. "
            "Ask for missing customer name, item, or quantity instead of guessing. "
            "Never claim an order was placed unless the tool confirms it. "
            "Keep replies short and friendly."
        ),
    }
]

print(
    "\nSweet Crumbs Agent is ready!\n"
    "Ask about prices, check an order, or request a new order.\n"
    "Type 'bye' to exit.\n"
)

while True:
    user_text = input("You: ").strip()

    if user_text.lower() == "bye":
        print("Agent: Thank you for visiting Sweet Crumbs. Goodbye!")
        break

    if not user_text:
        continue

    messages.append({"role": "user", "content": user_text})

    # Let the model request tools until it provides a final answer.
    for step in range(MAX_STEPS):
        response = llm_with_tools.invoke(messages)

        # Preserve the assistant message, including its tool requests.
        messages.append(response)

        if not response.tool_calls:
            print(f"Agent: {response.text}")
            break

        for call in response.tool_calls:
            name = call["name"]
            args = call["args"]

            if name not in TOOLS:
                result = f"Unknown tool: {name}"
            else:
                try:
                    result = TOOLS[name].invoke(args)
                except ValidationError:
                    result = (
                        f"Tool error: invalid arguments {args}. "
                        "Check the required argument names and types."
                    )
                except (ValueError, TypeError) as error:
                    result = f"Tool input error: {error}"

            print(f"  [tool] {name}({args}) -> {result}")

            # Match this result to the exact tool request.
            messages.append(
                {
                    "role": "tool",
                    "content": str(result),
                    "tool_call_id": call["id"],
                }
            )
    else:
        print(
            "Agent: Sorry, I could not finish this request. "
            "Please try again or ask a human for help."
        )
