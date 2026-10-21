
"""Lesson 2.4: Batch Product Writer."""

from time import perf_counter
from langchain.chat_models import init_chat_model

# Create the AI model once, outside the loop
writer = init_chat_model(
    "llama3.2",
    model_provider="ollama",
    temperature=0.7
)

# Bakery product dictionary
products = {
    "chocolate cake": 1500,
    "cupcake": 250,
    "brownie": 300,
    "old stock": 0,
    "donut": 200
}

# Store results and totals
results = []
total_tokens = 0
total_seconds = 0.0
start_time = perf_counter()

# Process each product
for name, price in products.items():

    # Skip products with no price
    if price == 0:
        print(f"Skipping {name} (no price)")
        continue

    prompt = (
        f"Write one tempting sentence of maximum 15 words "
        f"for '{name}' at {price} PKR, "
        "for a bakery menu in Lahore. "
        "Do not change the product name or price."
    )

    try:
        # Ask AI to generate a description
        call_start = perf_counter()
        response = writer.invoke([
            {"role": "user", "content": prompt}
        ])
        call_seconds = perf_counter() - call_start

        description = response.text.strip()

        # Save this product's result
        results.append({
            "item": name,
            "price": price,
            "text": description
        })

        # Collect token usage when available
        usage = response.usage_metadata or {}
        tokens = usage.get("total_tokens", 0)
        total_tokens += tokens

        # Measure elapsed time
        total_seconds += call_seconds

        print(f"Generated description for {name}")

    except Exception as error:
        print(f"Failed to process {name}: {error}")

# Print all successful results
print("=" * 50)
print("SWEET CRUMBS - BAKERY MENU")
print("=" * 50)

for number, row in enumerate(results, start=1):
    print(f"{number}. {row['item'].title()} ({row['price']} PKR)")
    print(f"   {row['text']}")

print("=" * 50)
print(f"Successful descriptions: {len(results)}")
print(f"Total tokens reported: {total_tokens}")
print(f"Total AI call time: {total_seconds:.1f} seconds")
print(f"Total program time: {perf_counter() - start_time:.1f} seconds")
