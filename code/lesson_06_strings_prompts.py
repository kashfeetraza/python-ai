
"""Task 1.6: Clean customer questions before sending them to AI."""

# Why: strip() removes extra spaces, and title() formats the name.
user_name = input("Your name: ").strip().title()

# Why: Cleaning the question makes the prompt easier to read.
question = input("Your question: ").strip().capitalize()

characters = len(question)
estimated_tokens = round(characters / 4)

print("=" * 40)
print(f"Cleaned question: {question}")
print(f"Characters: {characters}, about {estimated_tokens} tokens")

mentions_python = "python" in question.lower()
print(f"Mentions Python: {mentions_python}")
print("=" * 40)

# Stretch: Replace a bad word before building the prompt.
clean_question = question.replace("stupid", "***")

prompt = f"""You are a friendly Python tutor.
Greet {user_name} by name and answer in 3 short lines.
Question: {clean_question[:150]}"""

print(prompt)

# Stretch: Show an example cost estimate.
price_per_1k_tokens = 0.5
estimated_cost = estimated_tokens / 1000 * price_per_1k_tokens
print(f"Estimated cost: {estimated_cost:.2f} PKR")
