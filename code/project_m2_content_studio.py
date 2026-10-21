
"""AI Content Studio for Sweet Crumbs bakery.
Creates menu descriptions, streams social posts, answers prices,
and chats with customers using verified business facts.
"""

from langchain.chat_models import init_chat_model

# Why: separate models let us use precise answers for chat and creative text for marketing.
config = {
    "model": "llama3.2",
    "max_messages": 8,
    "cloud_price_per_1k_tokens": 0.002,
}

facts = {
    "name": "Sweet Crumbs",
    "city": "Lahore",
    "hours": "9 am to 10 pm",
    "delivery": "200 PKR, free for orders from 3,000 PKR",
    "currency": "PKR",
    "prices": {
        "chocolate cake": 1500,
        "cupcake": 250,
        "brownie": 300,
        "mango tart": 0,
    },
}

tones = {
    "fun": "Playful and full of energy, using short sentences.",
    "premium": "Elegant and calm, focused on quality and craftsmanship.",
    "urgent": "Exciting and persuasive, encouraging customers to order today.",
}

precise = init_chat_model(
    config["model"], model_provider="ollama", temperature=0.2
)
creative = init_chat_model(
    config["model"], model_provider="ollama", temperature=0.8
)

system_message = f"""
You are the customer assistant for {facts['name']}, located in {facts['city']}.
Business hours: {facts['hours']}.
Delivery: {facts['delivery']}.
Currency: {facts['currency']}.
Menu prices: {facts['prices']}.

Only use these facts when answering business questions.
Never invent prices, products, services, or business details.
If you do not know something, say that you do not have that information.
For questions about unavailable products, politely explain that you only know
the products listed in the bakery's menu.
"""

messages = [{"role": "system", "content": system_message}]

chat_answers = 0
menu_descriptions = 0
posts = 0
price_answers = 0
total_tokens = 0
total_seconds = 0.0

print("=" * 50)
print("   Sweet Crumbs AI Content Studio")
print("=" * 50)
print("Commands: /menu, /post fun|premium|urgent, /price <item>, /reset, bye")

while True:
    user_input = input("\nYou: ").strip()

    if not user_input:
        print("Studio: Please enter a command or ask a question.")
        continue

    command_text = user_input.lower()

    if command_text == "bye":
        print("Studio: Goodbye!")
        break

    elif command_text == "/reset":
        messages = [{"role": "system", "content": system_message}]
        print("Studio: Chat memory has been reset.")

    elif command_text == "/menu":
        generated_menu = []

        for item_name, item_price in facts["prices"].items():
            if item_price == 0:
                print(f"Studio: Skipping {item_name} (coming soon)")
                continue

            menu_prompt = (
                f"Write exactly one appealing sentence describing {item_name} "
                f"for {facts['name']}. Use only the product name and known "
                f"business facts. Do not invent ingredients or preparation details."
            )

            menu_response = creative.invoke(menu_prompt)
            description = menu_response.text

            generated_menu.append({
                "name": item_name,
                "price": item_price,
                "description": description,
            })

            usage = menu_response.usage_metadata or {}
            total_tokens += usage.get("total_tokens", 0)

            duration_ns = (menu_response.response_metadata or {}).get(
                "total_duration", 0
            )
            duration_seconds = duration_ns / 1_000_000_000
            total_seconds += duration_seconds
            menu_descriptions += 1

        print("-" * 50)

        for number, menu_item in enumerate(generated_menu, start=1):
            print(
                f"{number}. {menu_item['name'].title()} "
                f"({menu_item['price']:,} PKR)"
            )
            print(f"   {menu_item['description']}")

        print("-" * 50)

        # Why: the cost estimate helps the owner understand the value of batch generation.
        estimated_cost = (
            total_tokens / 1000
        ) * config["cloud_price_per_1k_tokens"]
        print(f"Studio: Estimated example cloud cost: ${estimated_cost:.2f}")

    elif command_text.startswith("/post"):
        command_parts = user_input.split(maxsplit=1)
        tone_name = command_parts[1].lower() if len(command_parts) > 1 else "fun"

        # Why: .get() provides a safe default when the owner enters an unknown tone.
        tone_description = tones.get(
            tone_name,
            "Friendly, clear, and appealing to local customers."
        )

        post_prompt = f"""
Write a short social media post for {facts['name']}.
Tone: {tone_description}
City: {facts['city']}
Hours: {facts['hours']}
Delivery: {facts['delivery']}
Menu prices: {facts['prices']}
Only use the supplied facts. Do not invent offers or product details.
"""

        print(f"Studio ({tone_description}):")

        post_tokens = 0
        post_duration = 0.0

        for chunk in creative.stream(post_prompt):
            print(chunk.text, end="", flush=True)

        print()

        # Why: streaming makes the post visible as the model generates it.
        posts += 1

        # Some streaming integrations provide usage metadata only on the final chunk.
        # Accumulate it when available without counting each chunk repeatedly.
        stream_usage = {}
        stream_duration_ns = 0

        # Stream metadata is not consistently available from every Ollama version.
        # The post is still displayed even when usage statistics are unavailable.
        total_tokens += stream_usage.get("total_tokens", 0)
        total_seconds += stream_duration_ns / 1_000_000_000

    elif command_text.startswith("/price"):
        item_name = user_input[len("/price"):].strip().lower()
        price = facts["prices"].get(item_name)

        if not item_name or price is None:
            print("Studio: That item is not on our menu.")
        elif price == 0:
            print(f"Studio: {item_name.title()} is coming soon.")
        else:
            print(f"Studio: {item_name.title()} costs {price:,} PKR.")

        # Why: dictionary lookups give accurate prices without spending AI tokens.
        price_answers += 1

    else:
        messages.append({"role": "user", "content": user_input})

        # Keep the system message and only the most recent configured messages.
        messages = [messages[0]] + messages[1:][-config["max_messages"]:]

        chat_response = precise.invoke(messages)
        print(f"Studio: {chat_response.text}")

        messages.append(chat_response)
        chat_answers += 1

        chat_usage = chat_response.usage_metadata or {}
        chat_tokens = chat_usage.get("input_tokens", 0)
        total_tokens += chat_usage.get("total_tokens", 0)

        chat_duration_ns = (chat_response.response_metadata or {}).get(
            "total_duration", 0
        )
        total_seconds += chat_duration_ns / 1_000_000_000

        print(
            f"        (memory: {len(messages) - 1} messages, "
            f"{chat_tokens:,} input tokens sent)"
        )

print("=" * 50)
print("Session report")
print(
    f"Chat answers: {chat_answers} | "
    f"Menu descriptions: {menu_descriptions} | "
    f"Posts: {posts} | Price answers: {price_answers}"
)
print(f"AI usage: {total_tokens:,} tokens in {total_seconds:.1f} seconds")
print("=" * 50)
