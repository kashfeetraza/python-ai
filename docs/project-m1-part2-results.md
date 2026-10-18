# Module 1 Checkpoint 2 — AI Test Results

**Important:** These results must contain real outputs from your local Ollama model. The project script prepares prompts but does not call Ollama automatically. Do not claim that an AI answer was tested until you have pasted the prompt into Ollama and saved its actual answer here.

## AI Test 1 — Product availability

**Prompt printed by the script (example):**

```text
You are the assistant of Sweet Crumbs bakery.
Answer Ali Raza in 2 short lines.
Use only confirmed business information. If you do not know an answer, say staff must confirm it.
Question: Do you make sugar-free cakes?
```

**Ollama model:** `qwen3.5:2b` (or write the exact model shown by `ollama list`)  
**Actual AI answer:** TODO — paste the answer from Ollama here.  
**Judgement:** TODO — useful or not, and why? Check whether it invents a menu item or price.

## AI Test 2 — Private order detail

**Prompt printed by the script (example):**

```text
You are the assistant of Sweet Crumbs bakery.
Answer Ali Raza in 2 short lines.
Use only confirmed business information. If you do not know an answer, say staff must confirm it.
Question: Can i change my phone number on the order?
```

**Routing expected:** local model label, zero estimated cloud cost.  
**Ollama model:** `qwen3.5:2b` (or write the exact model shown by `ollama list`)  
**Actual AI answer:** TODO — paste the answer from Ollama here.  
**Judgement:** TODO — useful or not, and why? Check that it does not promise a change was completed.

## How to run the two AI tests

1. Run the front desk script and enter the example questions.
2. Copy each full prompt printed under `Prompt:`.
3. In a second terminal, run `ollama run qwen3.5:2b` (if that model is installed).
4. Paste the prompt and save Ollama's actual response above.
5. Judge each answer honestly. If the model invents a price, timing, menu item, or promise, mention that.
