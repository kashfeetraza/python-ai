# Module 1 Checkpoint 2 — Front Desk Design

**Business:** Sweet Crumbs bakery  
**Bot:** Sweet Crumbs Desk

## Intents

| Intent | Keywords / test | Reply |
|---|---|---|
| Complaint (checked first) | `refund`, `complaint`, `late` | Apologize and say a manager will call within 1 hour. |
| Greeting | message starts with `hi`, `hello`, or `hey` | Greet the customer by name. |
| Hours | `hour`, `open`, `timing` | Open 9 am to 10 pm every day. |
| Location | `location`, `address`, `where` | Main Market, Lahore. |
| Delivery | `deliver`, `delivery` | Lahore delivery; 200 PKR or free when discounted subtotal is at least 3,000 PKR. |
| Price/menu | `fee`, `price`, `cost` | Show menu items and tell customer to use `/quote`. |
| Payment | `payment`, `pay` | Cash and bank transfer. |
| Quote | exact command `/quote` | Calculate a menu quote with optional bulk discount and delivery fee. |
| Exit | exact `bye` or `goodbye` | Say goodbye and print session report. |
| Fallback | anything not matched above | Prepare an AI prompt; route privacy-related questions locally. |

## Business rules

| Rule | Value |
|---|---|
| Cupcake | 250 PKR each |
| Brownie | 300 PKR each |
| Chocolate cake | 1,500 PKR each |
| Bulk discount | 10% off when quantity is 10 or more |
| Delivery | 200 PKR |
| Free delivery | Discounted subtotal is at least 3,000 PKR |
| Private words | `phone`, `cnic`, `my address`, `home address` |
| Local model label | `llama3.2 (local, private)`; estimated cost 0 PKR |
| Cloud model label | `small cloud model (cheap)` |
| Example cloud price | 0.1 PKR per 1,000 estimated tokens |
| Token estimate | rounded character count divided by 4 |
| Prompt limit | first 150 characters of the cleaned question |

**Rule order explanation:** complaints are checked before other intents so an unhappy customer reaches the human-handover response. Bulk discount is calculated before delivery eligibility. Therefore, 12 cupcakes have a 3,000 PKR subtotal, a 300 PKR discount, and a 2,700 PKR discounted subtotal; the 200 PKR delivery fee still applies.

## Rule tests

Run `uv run code/project_m1_front_desk.py` and enter the cases below one at a time. Mark Pass? honestly after running your own test.

| You type | Expected | Pass? |
|---|---|---|
| `  WHAT are your hours  ` | Hours reply; outer spaces and capitals handled | Pending |
| `which cake is best?` | Fallback, not a greeting | Pending |
| `my order is late` | Manager reply; complaint counter increases | Pending |
| `/quote`, item `chocolate cake`, quantity `1` | Subtotal 1,500 PKR; delivery 200 PKR | Pending |
| `/quote`, item `chocolate cake`, quantity `3` | Subtotal 4,500 PKR; delivery free | Pending |
| `/quote`, item `cupcake`, quantity `10` | 10% discount applied | Pending |
| `/quote`, item `pizza`, quantity `2` | Not on menu; no crash | Pending |
| Fallback question containing `phone` or `cnic` | Local model label and 0 cloud cost | Pending |
| Press Enter without text | Asks again; session continues | Pending |
| `BYE` | Goodbye and session report | Pending |
| `/quote`, quantity `many` | Polite quantity message; no crash | Pending |

## Notes for the live demo

- Show one FAQ, one discounted quote, and one fallback prompt.
- Explain that the fallback prompt is printed for the student to paste into Ollama; this Module 1 script does **not** call Ollama automatically.
- The report counts every non-empty chat message, including `bye`; quote commands count as rule-answered only when a valid menu quote is calculated.
- Replace each `Pending` value only after actually running that test.
