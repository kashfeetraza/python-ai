# AI Prompt Kit for a Local Business

A beginner-friendly Python project that turns a local business's details into three ready-to-use AI prompts. It helps business owners who want to use AI but are unsure what to ask.

**Course:** Python for AI  
**Module:** 1 — Python Basics for GenAI and Agentic AI  
**Project:** AI Prompt Kit for a Local Business

## Features

The program asks the user for five details:

- Business name
- Business type
- City
- Main customers
- Monthly budget in PKR

It then creates and prints three professional prompts:

1. **Marketing:** Generate a social media post idea for the business.
2. **Customer Service:** Draft a polite, professional response to an unhappy customer.
3. **Growth:** Suggest three low-cost AI tools or ideas within the monthly budget.

The prompts can be copied into an AI assistant such as Ollama, ChatGPT, or Claude.

## Concepts Practised

This project uses the Python basics covered in Module 1:

- `input()` to collect information from the user
- Variables to store business details
- `int()` to convert the monthly budget into an integer
- f-strings to insert business details into prompts
- `print()` to display the prompts
- Comments and a docstring to explain the code
- Prompt quality and awareness of AI hallucinations

## Requirements

- Python installed
- [`uv`](https://docs.astral.sh/uv/) installed
- An existing Python project with the script at `code/project_m1_prompt_kit.py`
- Ollama and a downloaded model if you want to test the prompts locally

The prompt generator itself uses Python's built-in features and does not need an AI model to run. Ollama is used separately to test the generated prompts.

## Run the Project

From the project root, run:

```powershell
uv run code/project_m1_prompt_kit.py
```

Answer the five questions when prompted. Enter the monthly budget as a number only, for example `100000`.

## Example

Example input:

```text
Business name: WebDevelopment
Business type: Full-Stack-Developer
City: Lahore
Main customers: All World
Monthly budget (PKR): 100000
```

The program displays a heading and three prompts. Example:

```text
=========================================
  AI Prompt Kit for WebDevelopment
=========================================

[1] Marketing
-----------------------------------------
Write a short Instagram post for WebDevelopment,
a Full-Stack-Developer in Lahore. Target international clients.
Use a friendly tone and include 1 call to action.

[2] Customer Service
-----------------------------------------
You are the manager of WebDevelopment. Write a polite
reply to a customer whose order arrived late. Apologise
and offer a small discount. Use a friendly and professional tone.

[3] Growth
-----------------------------------------
Suggest 3 low-cost AI tools or ideas that a Full-Stack-Developer
in Lahore can use to attract international clients, within a
monthly budget of 100000 PKR. Explain each idea briefly.
```

*The example is illustrative; the exact wording depends on the current version of the Python script.*

## Test the Prompts with Ollama

1. Make sure Ollama is running and a model is available.
2. Run the Python script and copy each generated prompt.
3. Paste each prompt into your selected Ollama model.
4. Save the actual AI answers and your evaluation in `docs/project-m1-results.md`.
5. Check whether the answers are relevant, practical, and within the stated budget. Verify tool names, prices, and factual claims instead of assuming the AI is always correct.

To see your installed Ollama models, run:

```powershell
ollama list
```

To start a model, replace the example model name with one installed on your computer:

```powershell
ollama run qwen3.5:2b
```

## Project Files

```text
python-ai/
├── code/
│   └── project_m1_prompt_kit.py
├── docs/
│   ├── project-m1-results.md
│   └── project-m1-run.png
└── README.md
```

This is the expected layout for the project deliverables; keep the paths consistent with your actual repository.

## Screenshot

When the screenshot is saved at the path below, it will appear in this README on GitHub:

![AI Prompt Kit running](docs/project-m1-run.png)

## Who Would Pay for This?

Small business owners, freelancers, and local service providers who want to use AI for marketing, customer communication, and business growth but need help writing effective prompts.

## What I Learned

Through this project, I practised collecting user input, storing values in variables, converting text to an integer, formatting strings, displaying clean output, and writing specific prompts. I also learned to test AI-generated responses critically and look for possible hallucinations.

## Future Improvements

- Connect the prompts directly to an AI model instead of copying and pasting.
- Add more prompt templates, such as WhatsApp replies and responses to Google reviews.
- Improve input validation and customize prompts for different types of businesses.
- Compare responses from two different AI models.

## Course

Python for AI — Module 1: Python Basics for GenAI and Agentic AI.
