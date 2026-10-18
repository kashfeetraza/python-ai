
"""Task 1.5: Create an AI model profile card with a cost estimate."""

# Why: These variables describe the model and use all four required types.
model_name = "llama3.2"
context_window = 128000
price_per_1k_tokens = 0.5
runs_locally = True

print("--- AI Model Profile Card ---")
print(f"Model: {model_name} {type(model_name)}")
print(f"Context window: {context_window} tokens {type(context_window)}")
print(f"Price per 1K tokens: {price_per_1k_tokens} PKR {type(price_per_1k_tokens)}")
print(f"Runs locally: {runs_locally} {type(runs_locally)}")

# Why: int() converts the user's input into a number for cost calculation.
tokens_per_chat = int(input("Tokens per chat: "))

estimated_cost = round(tokens_per_chat / 1000 * price_per_1k_tokens, 2)
print(f"Estimated cost: {estimated_cost} PKR")

# Stretch: Estimate the monthly cost for 30 days.
chats_per_day = int(input("Chats per day: "))
monthly_cost = round(estimated_cost * chats_per_day * 30, 2)
print(f"Estimated monthly cost: {monthly_cost} PKR")
