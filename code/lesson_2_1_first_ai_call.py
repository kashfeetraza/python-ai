
"""Lesson 2.1: Build a simple AI Tutor using LangChain and Ollama."""

from langchain.chat_models import init_chat_model

# Why: Get the topic and level so the tutor can customize its answer.
topic = input("Enter a topic: ").strip()
level = input("Enter your level (beginner or expert): ").strip().lower()

# Why: A system message controls the AI's role and answer length.
system_message = (
    f"You are a helpful AI tutor. Explain {topic} to a {level} student "
    "in 3 short sentences."
)

# Create the model with a low temperature for focused answers.
llm = init_chat_model(
    "llama3.2",
    model_provider="ollama",
    temperature=0.2,
)

# Ask the AI tutor for an answer.
response = llm.invoke([
    {"role": "system", "content": system_message},
    {"role": "user", "content": f"Teach me about {topic}."},
])

print("\nAI Tutor:", response.text)

# Print token usage and response time.
total_tokens = response.usage_metadata["total_tokens"]
seconds = response.response_metadata["total_duration"] / 1_000_000_000

print(f"Total tokens: {total_tokens}")
print(f"Time taken: {seconds:.1f} seconds")
