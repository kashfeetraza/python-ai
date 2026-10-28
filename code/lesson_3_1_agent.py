"""Lesson 3.1: organised Sweet Crumbs AI agent. Run from the code folder."""

from sweet_crumbs.agent import run_agent
from sweet_crumbs.config import MODEL, PROVIDER
from sweet_crumbs.data import business


def main() -> None:
    messages = [{
        "role": "system",
        "content": (
            f"You are the {business['name']} bakery assistant in {business['city']}. "
            "Use tools for prices, order status and new orders. Never guess prices or statuses. "
            "Ask for missing order details. Keep answers concise."
        ),
    }]
    print(f"{business['name']} Agent ({PROVIDER}: {MODEL}). Type 'bye' to exit.")
    while True:
        user_text = input("You: ").strip()
        if user_text.lower() == "bye":
            print("Agent: Goodbye!")
            break
        if not user_text:
            continue
        messages.append({"role": "user", "content": user_text})
        print(f"Agent: {run_agent(messages)}")


if __name__ == "__main__":
    main()
