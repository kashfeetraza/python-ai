
"""
Lesson 1.7: Operators and Making Decisions
Project: Smart Model Router
"""

# Ask the user for the task type.
task = input("Task (code / private / chat): ").strip().lower()

try:
    tokens = int(input("Estimated tokens: "))

    # Example prices per 1,000 tokens, for practice only.
    cloud_price = 0.50
    price = cloud_price

    # Why: private data should stay on the local model when privacy is required.
    # Why: routing simple tasks to a cheaper model can help reduce API costs.
    if task == "private":
        model = "qwen3.5:2b (local, Ollama)"
        price = 0.0
    elif task == "code":
        model = "Claude (cloud, coding)"
        price = cloud_price
    elif task == "chat":
        model = "Small cloud model (general chat)"
        price = cloud_price
    else:
        model = "Small cloud model (default)"
        price = cloud_price
        print("Unknown task type. Using the default model.")

    if tokens < 0:
        print("Error: Tokens cannot be negative.")
    else:
        # Calculate estimated cost.
        cost = (tokens / 1000) * price

        # Warn about long requests.
        if tokens > 4000:
            warning = "Long request: consider shortening it."
        else:
            warning = "Length is fine."

        # Stretch task: check the user's plan.
        paid_user = input("Is this a paid user? (yes/no): ").strip().lower()

        if paid_user == "no" and tokens > 2000:
            print("Upgrade to send long requests.")

        print("\n" + "=" * 40)
        print("--- Smart Model Router ---")
        print(f"Task: {task}")
        print(f"Tokens: {tokens:,}")
        print(f"Chosen model: {model}")
        print(f"Estimated cost: {cost:.2f} PKR")
        print(f"Warning: {warning}")
        print("=" * 40)

except ValueError:
    print("Invalid input! Please enter tokens as a whole number.")
