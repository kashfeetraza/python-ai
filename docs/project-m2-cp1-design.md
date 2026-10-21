
# Module 2 Checkpoint 1 — Design

## Facts

| Key | Value |
|---|---|
| name | Sweet Crumbs |
| city | Lahore |
| hours | 9 am to 10 pm |
| delivery | 200 PKR; free above 3,000 PKR |
| currency | PKR |
| prices | Chocolate cake: 1,500; Cupcake: 250; Brownie: 300; Mango tart: 0 |

## Tones

| Tone | Description sent to the AI |
|---|---|
| fun | Playful and energetic, with short sentences |
| premium | Elegant and calm, focused on quality |
| urgent | Exciting and persuasive, encouraging orders today |

## Model choices

| Job | Model and temperature | Why |
|---|---|---|
| Customer chat | precise, 0.2 | More consistent answers |
| Menu descriptions | creative, 0.8 | Varied marketing text |
| Social posts | creative, 0.8 | Different styles and ideas |
| Price lookup | No model | Exact dictionary values |

## Feature test results

Run each test and replace Pending with Pass or Fail.

| You type | Expected | Pass? |
|---|---|---|
| `/menu` | Numbered menu; mango tart skipped | Pending |
| `/post fun` | Fun post streams | Pending |
| `/post premium` | Premium post streams | Pending |
| `/post urgent` | Urgent post streams | Pending |
| `/post pirate` | Default tone; no KeyError | Pending |
| `/price CUPCAKE` | Correct price | Pending |
| `/price mango tart` | Coming soon | Pending |
| `/price pizza` | Not on menu | Pending |
| `My name is Ali`, then `What is my name?` | Remembers name | Pending |
| `/reset`, then `What is my name?` | Does not rely on previous chat | Pending |
| Press Enter | Asks again | Pending |
| `BYE` | Goodbye and report | Pending |
