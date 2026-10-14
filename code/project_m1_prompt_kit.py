

business_name = input("Business name: ")
business_type = input("Business type: ")
city = input("City: ")
customers = input("Main customers: ")
monthly_budget = int(input("Monthly budget (PKR): "))


print("\n=========================================")
print(f"  AI Prompt Kit for {business_name}")
print("=========================================")

marketing_prompt = (
    f"Write a short Instagram post for {business_name}, "
    f"a {business_type} in {city}. "
    f"Target {customers}. Use a friendly tone and include "
    f"1 call to action."
)

customer_service_prompt = (
    f"You are the manager of {business_name}. "
    f"Write a polite reply to a customer whose order arrived late. "
    f"Apologise and offer a small discount. "
    f"Use a friendly and professional tone."
)


growth_prompt = (
    f"Suggest 3 low-cost AI tools or ideas that a {business_type} "
    f"in {city} can use to attract {customers}, "
    f"within a monthly budget of {monthly_budget} PKR. "
    f"Explain each idea briefly and avoid unsupported price claims."
)


print("\n[1] Marketing")
print("-----------------------------------------")
print(marketing_prompt)

print("\n[2] Customer Service")
print("-----------------------------------------")
print(customer_service_prompt)

print("\n[3] Growth")
print("-----------------------------------------")
print(growth_prompt)

print("\n=========================================")
print("Your AI prompts are ready!")
print("Copy any prompt into Ollama, ChatGPT, or Claude.")
print("=========================================")
