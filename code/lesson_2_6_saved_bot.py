
"""Lesson 2.6: Saved Bakery Bot using JSON and error handling."""

import json

import httpx
import ollama
from langchain.chat_models import init_chat_model

FAQ_FILE = "faq.json"
HISTORY_FILE = "chat_history.json"
LOG_FILE = "errors.log"
MODEL = "llama3.2"


def log_error(message: str) -> None:
    """Append an error message to the log file."""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as log:
            log.write(message + "\n")
    except OSError:
        print("Warning: Could not write to the error log.")


def load_facts() -> dict:
    """Load business facts from the JSON file."""
    try:
        with open(FAQ_FILE, encoding="utf-8") as file:
            facts = json.load(file)

        if not isinstance(facts, dict):
            raise ValueError("FAQ must contain a JSON object.")

        required = {"name", "city", "hours", "delivery", "prices"}
        if not required.issubset(facts):
            raise ValueError("FAQ is missing required fields.")

        return facts

    except FileNotFoundError:
        raise SystemExit(
            f"Missing {FAQ_FILE}. Create it inside the code folder first."
        )
    except (json.JSONDecodeError, ValueError) as error:
        raise SystemExit(f"FAQ file is invalid: {error}")


def load_history(system: dict) -> list:
    """Load old messages, or start a new conversation."""
    try:
        with open(HISTORY_FILE, encoding="utf-8") as file:
            history = json.load(file)

        if not isinstance(history, list):
            raise ValueError("Chat history must be a JSON list.")

        # Keep only valid user and assistant messages.
        for message in history:
            if (
                not isinstance(message, dict)
                or message.get("role") not in {"user", "assistant"}
                or not isinstance(message.get("content"), str)
            ):
                raise ValueError("Invalid message in chat history.")

        print(f"Loaded {len(history)} old messages.")
        return [system] + history

    except FileNotFoundError:
        return [system]
    except (json.JSONDecodeError, ValueError) as error:
        print(f"History file was damaged ({error}). Starting fresh.")
        log_error(f"HistoryError: {error}")
        return [system]


def save_history(messages: list) -> None:
    """Save conversation messages as readable JSON."""
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(
            messages[1:],
            file,
            indent=2,
            ensure_ascii=False,
        )


def main() -> None:
    """Run the saved bakery chatbot."""
    facts = load_facts()

    llm = init_chat_model(
        MODEL,
        model_provider="ollama",
    )

    system = {
        "role": "system",
        "content": (
            f"You are the assistant of {facts['name']} "
            f"in {facts['city']}. "
            f"Business facts: {json.dumps(facts, ensure_ascii=False)}. "
            "Answer using only the provided facts. "
            "If information is unavailable, say you do not know. "
            "Reply in two short lines."
        ),
    }

    messages = load_history(system)

    print(f"\n{facts['name']} Bot")
    print("Ask about prices, hours, or delivery.")
    print("Commands: /reset, bye")

    while True:
        try:
            text = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! Your chat is saved.")
            break

        if text.lower() == "bye":
            print("Bot: Goodbye! Your chat is saved.")
            break

        if not text:
            continue

        if text.lower() == "/reset":
            messages = [system]
            try:
                save_history(messages)
                print("Bot: Memory cleared.")
            except OSError as error:
                print("Bot: Memory was cleared, but could not be saved.")
                log_error(f"SaveError: {error}")
            continue

        messages.append({"role": "user", "content": text})

        try:
            # Keep the latest six messages to limit context size.
            response = llm.invoke([system] + messages[1:][-6:])
            answer = response.text

            messages.append(
                {"role": "assistant", "content": answer}
            )

            try:
                save_history(messages)
            except OSError as error:
                print("Bot: Warning, chat history could not be saved.")
                log_error(f"SaveError: {error}")

            print(f"Bot: {answer}")

        except httpx.ConnectError:
            messages.pop()
            print(
                "Bot: I am offline right now. "
                "Please open the Ollama app and try again."
            )
            log_error("ConnectError: Ollama is not running.")

        except ollama.ResponseError as error:
            messages.pop()
            print("Bot: Sorry, something went wrong on my side.")
            log_error(f"ResponseError: {error}")

        except Exception as error:
            # Last-resort protection for unexpected runtime errors.
            messages.pop()
            print("Bot: An unexpected error occurred. Please try again.")
            log_error(f"UnexpectedError: {type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
