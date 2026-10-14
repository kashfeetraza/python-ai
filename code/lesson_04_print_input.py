
"""
Business Prompt Builder
Collects business details and creates a prompt for an AI model.
"""

# Personal details make the welcome message friendly.
name = input("Your name: ")
business = input("Business type: ")
problem = input("Biggest problem: ")

# A budget helps the AI recommend affordable solutions.
budget = int(input("Monthly budget in PKR: "))

print(f"\nWelcome, {name}!")
print("--- Your AI Prompt ---")

prompt = (
    f"Suggest 3 AI solutions for a {business} "
    f"that struggles with {problem}. "
    f"Budget: {budget} PKR per month."
)

# A single prompt is easier to copy into an AI model.
print(prompt)
