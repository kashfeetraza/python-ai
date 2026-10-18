
"""Task 1.7: Choose an AI model based on the task type."""

task_type = input("Task type (code/private/chat): ").strip().lower()
tokens = int(input("How many tokens? "))

# Why: Different tasks need different AI models.
if task_type == "code":
    model_name = "Claude (Cloud)"
    price_per_1k_tokens = 0.8

elif task_type == "private":
    model_name = "llama3.2 (Local Ollama)"
    price_per_1k_tokens = 0.0

else:
    model_name = "Gemini (Cloud)"
    price_per_1k_tokens = 0.1

# Why: Local models avoid per-token API charges.
estimated_cost = (tokens / 1000) * price_per_1k_tokens

print(f"\nSelected model: {model_name}")
print(f"Estimated cost: {estimated_cost:.2f} PKR")

if tokens > 4000:
    print("Warning: This request uses many tokens.")
else:
    print("Length is fine.")

# Stretch task: Check whether the user has a paid plan.
is_paid_user = input("Are you a paid user? (yes/no): ").strip().lower()

if is_paid_user == "no" and tokens > 2000:
    print("Upgrade to send long requests.")
