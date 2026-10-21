
"""Lesson 2.5: AI Skills Toolkit — reusable AI functions."""

from langchain.chat_models import init_chat_model

BUSINESS = "Sweet Crumbs"

# Create both models once and reuse them.
precise = init_chat_model(
    "llama3.2",
    model_provider="ollama",
    temperature=0.2,
)

creative = init_chat_model(
    "llama3.2",
    model_provider="ollama",
    temperature=0.8,
)


def estimate_tokens(text: str) -> int:
    """Estimate tokens using about four characters per token."""
    return round(len(text) / 4)


def ask_ai(
    prompt: str,
    system: str = "You are a helpful assistant. Answer in 2 short lines.",
    creative_mode: bool = False,
) -> str:
    """Send a prompt to the AI and return its answer as text."""
    if creative_mode:
        llm = creative
    else:
        llm = precise

    response = llm.invoke(
        [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ]
    )

    return response.text


def summarize(text: str, max_words: int = 30) -> str:
    """Summarize text in at most the requested number of words."""
    return ask_ai(
        f"Summarize in at most {max_words} words:\n{text}"
    )


def translate(text: str, language: str = "Urdu") -> str:
    """Translate text into the requested language."""
    return ask_ai(
        f"Translate into {language}. "
        f"Reply with the translation only:\n{text}"
    )


def reply_to_review(review: str, business: str) -> str:
    """Write a short, polite reply to a customer review."""
    return ask_ai(
        f"Write a 2-line polite reply from {business} "
        f"to this review:\n{review}",
        creative_mode=True,
    )


# Test a function that does not require an AI call.
assert estimate_tokens("Hello AI") == 2
assert estimate_tokens("") == 0

print("All tests passed!")

usage = {
    "summarize": 0,
    "translate": 0,
    "reply": 0,
}

print(f"\n{BUSINESS} AI Toolkit")
print("Commands: /summarize, /translate, /reply, bye")

while True:
    command = input("\nCommand: ").strip().lower()

    if command == "bye":
        break

    elif command == "/summarize":
        text = input("Text to summarize: ")
        print(f"AI: {summarize(text)}")
        usage["summarize"] += 1

    elif command == "/translate":
        text = input("Text to translate: ")
        language = input(
            "Language (press Enter for Urdu): "
        ).strip()

        if language == "":
            result = translate(text)
        else:
            result = translate(text, language)

        print(f"AI: {result}")
        usage["translate"] += 1

    elif command == "/reply":
        review = input("Customer review: ")

        result = reply_to_review(review, BUSINESS)
        print(f"AI: {result}")
        print(
            f"(Review was about {estimate_tokens(review)} tokens)"
        )

        usage["reply"] += 1

    else:
        print(
            "Unknown command. Try /summarize, "
            "/translate, /reply or bye."
        )

print("\nSkills used today:")
for skill, count in usage.items():
    print(f"  {skill}: {count}")
