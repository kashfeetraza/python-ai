
"""Lesson 2.3: Persona Bot with Real Facts."""

from langchain.chat_models import init_chat_model

# 1. Configuration dictionary
config = {
    "model": "llama3.2",
    "temperature": 0.3,
    "max_messages": 6
}

# 2. Real business facts
facts = {
    "name": "Sweet Crumbs",
    "city": "Lahore",
    "hours": "9 am to 10 pm",
    "prices": {
        "chocolate cake": 1500,
        "cupcake": 250,
        "brownie": 300
    }
}

# 3. Different chatbot personalities
personas = {
    "friendly": "warm and cheerful, uses simple words",
    "formal": "polite and professional, no jokes",
    "sales": "excited, always suggests one extra item to buy"
}

# 4. Initialize the AI model
llm = init_chat_model(
    config["model"],
    model_provider="ollama",
    temperature=config["temperature"]
)

# 5. Build system instructions using real facts
rules = (
    f"You are the assistant of {facts['name']} bakery in {facts['city']}. "
    f"Opening hours: {facts['hours']}. "
    f"Prices in PKR: {facts['prices']}. "
    "Only use these facts. Never invent prices or opening hours. "
    "If you do not know something, say you will check with the manager. "
    "Answer in 2 short lines."
)

# 6. Set the default personality
style = personas["friendly"]

messages = [
    {
        "role": "system",
        "content": f"{rules} Your style: {style}."
    }
]

print("Welcome to Sweet Crumbs Bakery!")
print("Commands: /persona friendly|formal|sales")
print("           /price <item>, bye")

# 7. Chat loop
while True:
    text = input("\nYou: ").strip()

    if text.lower() == "bye":
        print("Bot: Goodbye! Visit Sweet Crumbs again.")
        break

    # Switch the chatbot's personality
    elif text.lower().startswith("/persona "):
        name = text[9:].strip().lower()

        if name in personas:
            style = personas[name]
            messages[0]["content"] = (
                f"{rules} Your style: {style}."
            )
            print(f"Bot: Style changed to {name}.")
        else:
            print(
                "Bot: Invalid persona. Choose friendly, formal, or sales."
            )

    # Get prices directly from the dictionary
    elif text.lower().startswith("/price "):
        item = text[7:].strip().lower()

        if item in facts["prices"]:
            price = facts["prices"][item]
            print(f"Bot: {item.title()} costs {price} PKR.")
        else:
            print(f"Bot: Sorry, {item} is not on our menu.")

    elif text == "":
        print("Bot: Please type a message.")
    
    else:
        try:
            # Save the user's message
            messages.append({
                "role": "user",
                "content": text
            })

            # Keep system instructions and recent history
            messages = (
                [messages[0]]
                + messages[1:][-config["max_messages"]:]
            )

            # Ask the AI using conversation history
            response = llm.invoke(messages)
            answer = response.text

            # Save the assistant's reply
            messages.append({
                "role": "assistant",
                "content": answer
            })

            print(f"Bot: {answer}")

        except Exception as error:
            print(f"Bot: An error occurred: {error}")
