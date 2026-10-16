
"""
Lesson 1.5: Variables and Data Types
AI Model Profile Card and Cost Estimator
"""

# AI model profile
model_name: str = "qwen3.5:2b"
context_window: int = 32768
price_per_1k_tokens: float = 0.50  # Example price in PKR
runs_locally: bool = True

# Why: Clear variable names make the code easier to understand.
# Why: Type hints help developers identify the expected data types.

print("--- AI Model Profile Card ---")

print(f"Model name: {model_name} ({type(model_name).__name__})")
print(f"Context window: {context_window} ({type(context_window).__name__})")
print(
    f"Price per 1K tokens: {price_per_1k_tokens} PKR "
    f"({type(price_per_1k_tokens).__name__})"
)
print(f"Runs locally: {runs_locally} ({type(runs_locally).__name__})")

try:
    # input() returns text, so convert it to int before calculations.
    tokens_used = int(input("\nHow many tokens does one chat use? "))
    chats_per_day = int(input("How many chats per day? "))

    if tokens_used < 0 or chats_per_day < 0:
        print("Please enter zero or a positive whole number.")
    else:
        # Calculate estimated cost.
        cost_per_chat = (tokens_used / 1000) * price_per_1k_tokens
        daily_cost = cost_per_chat * chats_per_day
        monthly_cost = daily_cost * 30

        print("\n--- Cost Estimate ---")
        print(f"Cost per chat: {cost_per_chat:.2f} PKR")
        print(f"Daily cost: {daily_cost:.2f} PKR")
        print(f"Monthly cost (30 days): {monthly_cost:.2f} PKR")

except ValueError:
    print("Invalid input! Please enter whole numbers, such as 1200 or 50.")
