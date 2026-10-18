
"""Task 1.8: Build a rule-based business helper chatbot."""

business_name = "City Care Clinic"
message_count = 0
unanswered_count = 0
complaint_count = 0

# Why: Store business replies in one place so they are easy to update.
intents = {
    "hours": {
        "keywords": ["hours", "open", "timing"],
        "reply": "Our clinic timings are 9 AM to 8 PM."
    },
    "location": {
        "keywords": ["location", "address", "where"],
        "reply": "Please check our official page for the clinic address."
    },
    "appointment": {
        "keywords": ["appointment", "book", "booking"],
        "reply": "Please contact our reception to book an appointment."
    },
    "services": {
        "keywords": ["services", "treatment", "doctor"],
        "reply": "We provide general consultations and basic healthcare services."
    },
    "fees": {
        "keywords": ["fee", "fees", "price", "cost"],
        "reply": "Please contact reception for the latest consultation fees."
    }
}

print(f"Welcome to {business_name}!")
user_name = input("What is your name? ").strip().title()

print(f"Hello, {user_name}! How can I help you?")
print("Ask about hours, location, appointments, services, or fees.")
print("Type 'bye' to exit.")

while True:
    message = input("\nYou: ").strip().lower()

    if message == "bye":
        break

    message_count += 1

    # Why: Handle complaints before normal questions.
    if "complaint" in message or "problem" in message:
        complaint_count += 1
        print("Bot: I'm sorry about that. Please contact our reception for help.")

    elif "agent" in message or "human" in message:
        print("Bot: Connecting you to a human...")
        break

    elif message == "hi" or message.startswith("hi "):
        print(f"Bot: Hello, {user_name}! How can I help?")

    else:
        answered = False

        for intent in intents.values():
            for keyword in intent["keywords"]:
                if keyword in message:
                    print(f"Bot: {intent['reply']}")
                    answered = True
                    break

            if answered:
                break

        if not answered:
            unanswered_count += 1
            print("Bot: I don't know that answer yet.")
            print("A future AI prompt could be:")
            print(f"Answer this customer question for {business_name}: {message}")

print("\n--- Chat Summary ---")
print(f"Thank you, {user_name}!")
print(f"Messages received: {message_count}")
print(f"Unanswered questions: {unanswered_count}")
print(f"Complaints received: {complaint_count}")
print("Goodbye!")
