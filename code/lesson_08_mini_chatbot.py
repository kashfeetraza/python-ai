
"""
Lesson 1.8: Rule-Based Chatbot
Business: Sweet Crumbs Bakery

A beginner-friendly chatbot that answers common customer questions.
"""

BOT = "Sweet Crumbs Bot"

print(f"{BOT}: Welcome! I can help with prices, hours, location and orders.")
print(f"{BOT}: Type 'bye' to end the chat.")

# Ask the name once so the bot remembers it throughout the conversation.
name = input(f"{BOT}: What is your name? ").strip().title()

if name == "":
    name = "Friend"

print(f"{BOT}: Nice to meet you, {name}!")

message_count = 0
unanswered_count = 0
complaint_count = 0

while True:
    message = input(f"{name}: ").strip().lower()
    message_count += 1

    # Why: an exit check prevents the chatbot from running forever.
    if message == "bye" or message == "exit":
        print(f"{BOT}: Goodbye, {name}! Thanks for visiting.")
        break

    elif message == "":
        print(f"{BOT}: Please type a question.")

    # Why: handle complaints before orders so unhappy customers get priority.
    elif (
        "refund" in message
        or "complaint" in message
        or "late" in message
    ):
        complaint_count += 1
        print(
            f"{BOT}: Sorry about that, {name}. "
            "A manager will contact you within 1 hour."
        )

    elif "agent" in message or "human" in message:
        print(f"{BOT}: Connecting you to a human...")
        break

    elif "hour" in message or "open" in message or "time" in message:
        print(f"{BOT}: We are open every day, from 9 AM to 10 PM.")

    elif "price" in message or "cost" in message or "how much" in message:
        print(
            f"{BOT}: Cakes start at 1,500 PKR. "
            "Cupcakes cost 250 PKR each."
        )

    elif "where" in message or "location" in message or "address" in message:
        print(f"{BOT}: Our example business is on Main Boulevard, Lahore.")

    elif "order" in message or "delivery" in message:
        print(
            f"{BOT}: You can place an order through our business WhatsApp. "
            "Delivery is free on orders over 3,000 PKR."
        )

    elif (
        message in ("hi", "hello", "hey")
        or message.startswith("salam")
    ):
        print(f"{BOT}: Hello, {name}! How can I help you?")

    else:
        unanswered_count += 1

        # Why: unanswered questions help us discover missing chatbot rules.
        # Why: this prompt shows how an LLM could answer in Module 2.
        prompt = (
            "You are a friendly assistant for Sweet Crumbs Bakery. "
            f"Answer the customer in 2 short sentences. Question: {message}"
        )

        print(f"{BOT}: I don't know that answer yet.")
        print(f"{BOT}: Example AI prompt: {prompt}")

print("\n" + "=" * 40)
print("CHAT SUMMARY")
print("=" * 40)
print(f"Customer: {name}")
print(f"Messages received: {message_count}")
print(f"Unanswered questions: {unanswered_count}")
print(f"Complaints received: {complaint_count}")
print("Thank you for testing the chatbot!")
