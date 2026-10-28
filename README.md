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



## Task 1.8: Business Helper Bot Design

Business: City Care Clinic

| Intent | User wants | Keywords | Reply |
|---|---|---|---|
| Hours | Know opening times | hours, open, timing | Our clinic timings are 9 AM to 8 PM. |
| Location | Find the clinic | location, address, where | Check our official page for the address. |
| Appointment | Book a visit | appointment, book, booking | Contact reception to book an appointment. |
| Services | Know available services | services, treatment, doctor | We provide general consultations and basic healthcare services. |
| Fees | Know consultation cost | fee, fees, price, cost | Contact reception for current fees. |



# Sweet Crumbs AI Front Desk

A beginner-friendly Python front desk for a local bakery: it answers common questions with rules, calculates menu quotes, prepares AI-ready prompts, keeps privacy-related questions on a local-model route, and prints a session report.

## Requirements

- Python 3.13 or newer
- `uv`
- Optional for the AI tests: Ollama and a locally installed model such as `qwen3.5:2b`

## Run

From the project root:

```powershell
uv run code/project_m1_front_desk.py
```

This script uses only Python Module 1 concepts and the Python standard library. It does not automatically send prompts to Ollama; copy the printed prompt into your local model during the AI test.

## Project files

- `code/project_m1_front_desk.py` — working front desk script
- `docs/project-m1-part2-design.md` — intents, business rules, and rule test table
- `docs/project-m1-part2-results.md` — AI test record to complete with real Ollama answers
- `docs/project-m1-part2-run.png` — add your own screenshot after running a full session

## Screenshot

After running a complete session, take a screenshot that includes a FAQ answer, a quote, an AI-ready prompt, and the final session report. Save it as `docs/project-m1-part2-run.png`.

## Business value

The bot can save staff time by answering repeat questions and calculating consistent quotes automatically, while keeping a record of customer questions so the owner can improve service.

## Demo

1. Introduce Sweet Crumbs and the repeated-question problem.
2. Show an FAQ, a quote with a discount, and a fallback prompt.
3. Explain the session report and why discount is applied before checking free delivery.
4. Show the two real Ollama test results and discuss any hallucination or limitation.

## Submission checklist

- [ ] Run the script and complete the rule-test table honestly.
- [ ] Paste two real Ollama answers and your judgement into `docs/project-m1-part2-results.md`.
- [ ] Save a full-session screenshot as `docs/project-m1-part2-run.png`.
- [ ] Practise explaining the code in your own words.
- [ ] Commit with: `Module 1 Checkpoint 2 Project: AI Front Desk`



# AI Quality Test Results

Run the application and record the actual responses.

## Test 1 — Business hours

**Question:** What are your opening hours?

**AI answer:** Replace with the actual answer.

**Judgement:** Correct or hallucinated? Explain briefly.

## Test 2 — Price

**Question:** How much does a cupcake cost?

**AI answer:** Replace with the actual answer.

**Judgement:** Correct or hallucinated? Explain briefly.

## Test 3 — Unknown product

**Question:** Do you sell pizza?

**AI answer:** Replace with the actual answer.

**Judgement:** Correct or hallucinated? Explain briefly.

## Best social media post

**Tone:** Replace with your chosen tone.

**Actual post:** Paste the post produced by your application.

**Why this tone works best:** Explain why it suits Sweet Crumbs.


# Lesson 3.1 — Organised Sweet Crumbs Agent

## Important: preserve your current data
This bundle intentionally does **not** include a live `business.json`. Keep your existing `business.json` in this folder so your existing orders are not overwritten. If it lacks `hours`, `delivery`, `order_prefix`, or `next_order_number`, add those fields carefully while preserving its current `prices` and `orders`. `business.json.example` is only a template.

## Install dependencies
Run these commands from your existing `code` folder (the folder containing `pyproject.toml`):

```powershell
uv add python-dotenv langchain langchain-ollama
```

If these dependencies are already installed, this simply ensures they're declared in the project.

## Set up secrets/settings
Copy `.env.example` to `.env` and keep `.env` untracked:

```powershell
Copy-Item .env.example .env
```

Default model setting uses the local Ollama model `llama3.2:latest`. Make sure it is available using `ollama list`.

## Run from the code folder
```powershell
uv run lesson_3_1_agent.py
```

Other lesson checks:
```powershell
uv run sweet_crumbs/pricing.py
uv run lesson_3_1_imports.py
uv run lesson_3_1_env.py
git status
```

Check that `.env` is not shown by `git status`, but `.env.example` is allowed to be committed.
