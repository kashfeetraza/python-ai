name = "Kashfeet Raza"
goal = "AI Agent Developer"
print(f"Hi, I am {name} and I will become an {goal}.")



# 2. print(): Show Output

print("Hello, AI world!")
print("Model:", "gemma4:31b-cloud")             # comma adds a space
print("Python", "for", "AI", sep="-")   # Python-for-AI
print("Thinking", end="... ")           # stay on the same line
print("done")                           # Thinking... done


# **f-strings (most used in AI code):** put variables inside `{ }`.

model = "deepseek"
tokens = 120
print(f"{model} used {tokens} tokens")




# Multi-line text (great for prompts):**

prompt = """You are a helpful tutor.
Explain Python in 2 lines."""
print(prompt)


# 3. input(): Get User Input


name = input("Your name: ")
print(f"Welcome, {name}!")


# **Golden rule:** `input()` **always returns text (str)**, even if the user types a number.

age = input("Age: ")          # "20" (text)
age = int(input("Age: "))     # 20 (number)
print(age + 1) 


# 5. Mini Build: Prompt Builder

"""Lesson 1.4: Build a prompt from user input."""

# Collect details from the user
role = input("AI role (e.g. engineer): ")
topic = input("Topic: ")
level = input("Level (beginner/expert): ")

# Build the final prompt (this is what we will send to an LLM later)
prompt = f"You are a {role}. Explain {topic} to a {level} in 3 bullet points."

print("\n--- Your Prompt ---")
print(prompt)


