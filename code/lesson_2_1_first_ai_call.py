
"""Lesson 2.1: AI Tutor using LangChain and Ollama."""

from langchain.chat_models import init_chat_model

# Create the model once and reuse it.
llm = init_chat_model(
    "llama3.2",
    model_provider="ollama",
    temperature=0.2,
)

print("=== Your AI Tutor ===")

topic = input("Enter a topic to learn: ").strip()
level = input("Enter your level (beginner/intermediate/advanced): ").strip()

if not topic or not level:
    print("Please enter both a topic and a learning level.")
else:
    messages = [
        {
            "role": "system",
            "content": (
                "You are a friendly AI tutor. "
                "Explain topics at the student's requested level. "
                "Use simple examples and clear language. "
                "Keep the answer focused and beginner-friendly when appropriate."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Teach me about {topic}. "
                f"My learning level is {level}. "
                "Explain the key idea, give one example, and finish with "
                "one short practice question."
            ),
        },
    ]

    try:
        print("\nTutor is preparing your lesson...\n")

        response = llm.invoke(messages)

        # Print the AI's answer.
        print("=== Tutor's Answer ===")
        print(response.text)

        # Read token usage safely.
        usage = response.usage_metadata or {}
        input_tokens = usage.get("input_tokens", 0)
        output_tokens = usage.get("output_tokens", 0)
        total_tokens = usage.get(
            "total_tokens",
            input_tokens + output_tokens,
        )

        # Ollama may provide duration in nanoseconds.
        metadata = response.response_metadata or {}
        duration_ns = metadata.get("total_duration")

        print("\n=== Usage Information ===")
        print(f"Input tokens:  {input_tokens}")
        print(f"Output tokens: {output_tokens}")
        print(f"Total tokens:  {total_tokens}")

        if duration_ns is not None:
            seconds = duration_ns / 1_000_000_000
            print(f"Response time: {seconds:.2f} seconds")
        else:
            print("Response time: Not provided by the model metadata.")

    except Exception as error:
        print(f"\nSomething went wrong: {error}")
        print("Check that Ollama is running and llama3.2 is installed.")
