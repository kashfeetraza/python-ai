"""Rule-based and AI-ready front desk assistant for Sweet Crumbs bakery.

It answers common bakery questions, calculates quotes, prepares safe AI prompts,
and reports what customers asked during one session.
"""

BOT_NAME = "Sweet Crumbs Desk"
BUSINESS_NAME = "Sweet Crumbs bakery"
DELIVERY_FEE = 200
FREE_DELIVERY_LIMIT = 3000
CLOUD_PRICE_PER_1K_TOKENS = 0.1
LOCAL_MODEL_NAME = "llama3.2 (local, private)"
CLOUD_MODEL_NAME = "small cloud model (cheap)"
BULK_DISCOUNT_RATE = 0.10
BULK_DISCOUNT_QUANTITY = 10

# Keep business details in constants so staff can update them in one place.
OPENING_HOURS = "We are open 9 am to 10 pm, every day."
BUSINESS_LOCATION = "We are at Main Market, Lahore."
DELIVERY_INFO = "We deliver in Lahore. Delivery costs 200 PKR, or is free when the discounted subtotal is at least 3,000 PKR."
PAYMENT_INFO = "We accept cash and bank transfer."
MENU_INFO = "Our menu includes cupcakes, brownies, and chocolate cake."

print("=" * 50)
print(f"   {BOT_NAME}: rules, quotes and AI-ready prompts")
print("=" * 50)
print("Ask anything, type /quote for a price, or bye to exit.")

customer_name = input(f"{BOT_NAME}: What is your name? ").strip().title()
if customer_name == "":
    customer_name = "Customer"

message_count = 0
rules_answered = 0
unanswered_count = 0
quote_count = 0
total_quoted_value = 0.0
total_estimated_ai_cost = 0.0
complaint_count = 0

while True:
    user_message = input(f"{customer_name}: ").strip().lower()

    # Empty messages are not counted because they contain no customer question.
    if user_message == "":
        print(f"{BOT_NAME}: Please type a question, /quote, or bye.")
        continue

    message_count += 1

    # Complaint handling comes first so a complaint cannot be hidden by another rule.
    if "refund" in user_message or "complaint" in user_message or "late" in user_message:
        print(f"{BOT_NAME}: Sorry about that. A manager will call you within 1 hour.")
        rules_answered += 1
        complaint_count += 1

    elif user_message == "bye" or user_message == "goodbye":
        print(f"{BOT_NAME}: Goodbye, {customer_name}!")
        break

    elif user_message.startswith("hi") or user_message.startswith("hello") or user_message.startswith("hey"):
        print(f"{BOT_NAME}: Hello, {customer_name}! How can I help you?")
        rules_answered += 1

    elif "hour" in user_message or "open" in user_message or "timing" in user_message:
        print(f"{BOT_NAME}: {OPENING_HOURS}")
        rules_answered += 1

    elif "location" in user_message or "address" in user_message or "where" in user_message:
        print(f"{BOT_NAME}: {BUSINESS_LOCATION}")
        rules_answered += 1

    elif "deliver" in user_message or "delivery" in user_message:
        print(f"{BOT_NAME}: {DELIVERY_INFO}")
        rules_answered += 1

    elif "fee" in user_message or "price" in user_message or "cost" in user_message:
        print(f"{BOT_NAME}: {MENU_INFO} Type /quote for an exact price.")
        rules_answered += 1

    elif "payment" in user_message or "pay" in user_message:
        print(f"{BOT_NAME}: {PAYMENT_INFO}")
        rules_answered += 1

    elif user_message == "/quote":
        item_name = input(f"{BOT_NAME}: Which item? ").strip().lower()
        quantity_text = input(f"{BOT_NAME}: How many? ").strip()

        # Checking digits first prevents invalid quantity text from crashing the program.
        if not quantity_text.isdigit() or int(quantity_text) <= 0:
            print(f"{BOT_NAME}: Please enter a whole-number quantity greater than zero.")
        else:
            quantity = int(quantity_text)

            if item_name == "cupcake" or item_name == "cupcakes":
                item_price = 250
                clean_item_name = "cupcake"
            elif item_name == "brownie" or item_name == "brownies":
                item_price = 300
                clean_item_name = "brownie"
            elif item_name == "chocolate cake" or item_name == "cake":
                item_price = 1500
                clean_item_name = "chocolate cake"
            else:
                item_price = 0
                clean_item_name = item_name

            if item_price == 0:
                print(f"{BOT_NAME}: Sorry, {item_name} is not on our menu.")
            else:
                subtotal = item_price * quantity
                discount = 0

                # Apply the bulk discount before checking the delivery threshold.
                if quantity >= BULK_DISCOUNT_QUANTITY:
                    discount = subtotal * BULK_DISCOUNT_RATE

                discounted_subtotal = subtotal - discount

                # Delivery is free only when the discounted subtotal reaches the limit.
                if discounted_subtotal >= FREE_DELIVERY_LIMIT:
                    delivery_cost = 0
                else:
                    delivery_cost = DELIVERY_FEE

                quote_total = discounted_subtotal + delivery_cost
                quote_count += 1
                total_quoted_value += quote_total
                rules_answered += 1

                print(f"{BOT_NAME}: {quantity:,} x {clean_item_name} = {subtotal:,.0f} PKR")
                print(f"     Discount: -{discount:,.0f} PKR | Delivery: {delivery_cost:,.0f} PKR")
                print(f"     Total: {quote_total:,.0f} PKR")

    else:
        # Slice the question to keep the prepared prompt short and predictable.
        cleaned_question = user_message.capitalize()[:150]
        estimated_tokens = round(len(cleaned_question) / 4)

        # Private information stays local so it is not sent to a cloud provider.
        if "phone" in user_message or "cnic" in user_message or "my address" in user_message or "home address" in user_message:
            chosen_model = LOCAL_MODEL_NAME
            estimated_cost = 0.0
        else:
            chosen_model = CLOUD_MODEL_NAME
            estimated_cost = estimated_tokens / 1000 * CLOUD_PRICE_PER_1K_TOKENS
            total_estimated_ai_cost += estimated_cost

        unanswered_count += 1
        print(f"{BOT_NAME}: Good question! Routed to: {chosen_model} (~{estimated_tokens} tokens)")
        prompt = f"""You are the assistant of {BUSINESS_NAME}.
Answer {customer_name} in 2 short lines.
Use only confirmed business information. If you do not know an answer, say staff must confirm it.
Question: {cleaned_question}"""
        print("     Prompt:")
        print(f"     {prompt}")

print("=" * 50)
print("Session report")
print(f"Messages: {message_count} | Answered by rules: {rules_answered} | Unanswered: {unanswered_count}")
print(f"Quotes: {quote_count} | Quoted value: {total_quoted_value:,.0f} PKR")
print(f"Estimated AI cost for unanswered questions: {total_estimated_ai_cost:.4f} PKR")
print(f"Complaints handed to staff: {complaint_count}")
print("=" * 50)
