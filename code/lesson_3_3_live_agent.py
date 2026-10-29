
"""Lesson 3.3: Sweet Crumbs assistant with live API tools."""

from sweet_crumbs.agent import run_agent
from sweet_crumbs.config import MODEL, PROVIDER
from sweet_crumbs.data import business


SYSTEM_PROMPT = f"""
You are the AI assistant for Sweet Crumbs bakery.

Business information:
{business}

Follow these rules carefully:

1. Never invent product prices, exchange rates, weather data,
   order details, or other factual information.

2. When asked about a product price, use the get_price tool.
   Use the exact numeric price returned by the tool.

3. When asked for a product price in another currency:
   - First call get_price with the product name.
   - Read the actual numeric price returned by get_price.
   - Then call convert_currency with:
       amount = the numeric price from get_price
       from_currency = "PKR"
       to_currency = the requested currency
   - Never pass "get_price", a product name, or another string
     as the amount argument.
   - Do not guess the exchange rate or calculate using an
     exchange rate remembered from previous conversations.

4. When asked about current weather, use get_weather.

5. If a tool returns an error, explain the error honestly.
   Never replace failed tool results with invented information.

6. Only state that an action was completed if the appropriate
   tool confirms that it succeeded.

7. Keep responses clear, helpful, and concise.
"""


def main() -> None:
    print(f"Sweet Crumbs ({PROVIDER}: {MODEL})")
    print("Try: How much is a chocolate cake in USD?")
    print("Or: What is the current weather in Lahore?")
    print("Type 'bye' to exit.")

    # Keep the system prompt as the first message.
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in {"bye", "exit", "quit"}:
                print("Assistant: Goodbye! Have a great day.")
                break

            if not user_input:
                continue

            messages.append({
                "role": "user",
                "content": user_input,
            })

            result = run_agent(messages)

            # Support common return types from existing agent code.
            if isinstance(result, str):
                answer = result

            elif isinstance(result, dict):
                answer = (
                    result.get("output")
                    or result.get("content")
                    or result.get("messages", [{}])[-1].get("content")
                    or str(result)
                )

            else:
                answer = str(result)

            print(f"Agent: {answer}")

            # Some agent implementations return the complete
            # conversation; others return only the final answer.
            if isinstance(result, dict) and isinstance(
                result.get("messages"), list
            ):
                messages = result["messages"]
            else:
                messages.append({
                    "role": "assistant",
                    "content": answer,
                })

        except KeyboardInterrupt:
            print("\nAssistant: Goodbye!")
            break

        except Exception as error:
            print(f"Assistant error: {error}")
            print("Please try again.")

    print("Session ended.")


if __name__ == "__main__":
    main()
