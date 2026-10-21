
"""Lesson 2.2: Personal Tutor with Memory."""

from langchain.chat_models import init_chat_model

MAX_MESSAGES = 6

# Create the AI model
llm = init_chat_model(
    "llama3.2",
    model_provider="ollama"
)

# System message: the tutor's permanent instructions
messages = [
    {
        "role": "system",
        "content": (
            "You are a friendly personal Python tutor. "
            "Explain concepts in simple English and keep answers short."
        )
    }
]

print("Personal Tutor: Ask me anything!")
print("Commands: /reset, /count, bye")

while True:
    text = input("\nYou: ").strip()

    # Exit the chatbot
    if text.lower() == "bye":
        print("Tutor: Goodbye! Keep learning Python.")
        break

    # Clear conversation history
    elif text.lower() == "/reset":
        messages = [messages[0]]
        print("Tutor: Memory cleared.")
        continue

    # Count messages currently stored
    elif text.lower() == "/count":
        print(f"Tutor: {len(messages) - 1} conversation messages.")
        continue

    # Handle empty input
    elif text == "":
        print("Tutor: Please type a question.")
        continue

    # Save the user's message
    messages.append({
        "role": "user",
        "content": text
    })

    # Keep only the newest messages, preserving system instructions
    messages = [messages[0]] + messages[1:][-MAX_MESSAGES:]

    try:
        # Send conversation history to the AI
        response = llm.invoke(messages)

        # Get the AI's answer
        answer = response.text

        # Save the AI's reply for future turns
        messages.append({
            "role": "assistant",
            "content": answer
        })

        print(f"Tutor: {answer}")

        # Display token usage when the model provides it
        usage = response.usage_metadata or {}
        input_tokens = usage.get("input_tokens")

        if input_tokens is not None:
            print(f"(Memory: {len(messages) - 1} messages, "
                  f"{input_tokens} input tokens sent)")
        else:
            print(f"(Memory: {len(messages) - 1} messages, "
                  "token usage unavailable)")

    except Exception as error:
        print(f"Tutor: An error occurred: {error}")
