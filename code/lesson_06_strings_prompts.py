
"""
Lesson 1.6: Working with Text (Strings)
Project: Prompt Cleaner for an AI chatbot.
"""

# Ask the user for their name and question.
raw_name = input("Enter your name: ")
raw_question = input("Enter your question: ")

# Why: strip() removes extra spaces that users may accidentally type.
name = raw_name.strip().title()
question = raw_question.strip().capitalize()

# Why: clean text makes prompts easier to read and process.
# Replace an example unwanted word before sending text to the model.
clean_question = question.replace("stupid", "***")

# Estimate the number of tokens.
characters = len(clean_question)
estimated_tokens = round(characters / 4)

# Check whether the question mentions Python, regardless of capitalization.
mentions_python = "python" in clean_question.lower()

# Limit the question to 150 characters to keep the prompt shorter.
short_question = clean_question[:150]

# Example practice price only, not a real API price.
price_per_1k_tokens = 0.50
estimated_cost = (estimated_tokens / 1000) * price_per_1k_tokens

print("\n" + "=" * 40)
print("--- Prompt Cleaner Results ---")
print(f"Name: {name}")
print(f"Cleaned question: {clean_question}")
print(f"Characters: {characters}")
print(f"Estimated tokens: {estimated_tokens}")
print(f"Mentions Python: {mentions_python}")
print(f"Estimated cost: {estimated_cost:.2f} PKR")
print("=" * 40)

# Build a multi-line prompt using an f-string.
prompt = f"""You are a helpful Python tutor.
Greet the user by name: {name}
Answer the user's question in 3 simple lines.
User question: {short_question}
"""

print("\n--- Final AI Prompt ---")
print(prompt)

