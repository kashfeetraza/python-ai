# Hallucination Hunt — Task 2.7

**Project:** Sweet Crumbs AI Order Extractor  
**Purpose:** To test whether the AI extracts customer orders correctly without inventing information.

## 1. Test Cases

### Test 1: Normal Order
**Message:** I want 2 brownies. My name is Ali.

**Expected Result:** The AI should extract the item as brownie, quantity as 2, and customer name as Ali.

**Result:** The order should be accepted if all extracted information is correct and brownie is available on the menu.

### Test 2: Multiple Items
**Message:** Salam! 2 cupcakes aur 1 chocolate cake chahiye. Ali, house 12 Gulberg.

**Expected Result:** The AI should extract 2 cupcakes, 1 chocolate cake, customer name Ali, and address house 12 Gulberg.

**Result:** Python should calculate the total using the actual menu prices.

### Test 3: Item Not on Menu
**Message:** I want 1 pizza. My name is Bilal.

**Expected Result:** The AI should identify pizza as an item that is not available on the menu.

**Result:** The program should display a CHECK warning and must not assign a price to pizza.

### Test 4: Not an Order
**Message:** Hi, do you deliver to Johar Town?

**Expected Result:** The AI should identify that this is a question, not an order.

**Result:** The program should not save it as a valid order.

### Test 5: Missing Customer Name
**Message:** I want 3 brownies.

**Expected Result:** The AI should not invent a customer name.

**Result:** The program should flag the missing customer name for manual checking.

## 2. Hallucinations and Errors to Check

- Did the AI invent a customer name?
- Did it extract an item that was not mentioned in the message?
- Did it accept an item that was not on the menu?
- Did it calculate the total incorrectly?
- Did it mistake a delivery question for an order?

## 3. How I Prevented Hallucinations

1. I used a JSON schema to structure the AI's response.
2. I used Python to validate the extracted information.
3. I checked every item against the menu.
4. I calculated order totals using Python and actual menu prices.
5. I checked that the customer's name appeared in the original message.
6. I handled invalid JSON responses and displayed CHECK warnings for suspicious data.

## 4. Conclusion

The Hallucination Hunt helps identify mistakes made by the AI Order Extractor. Validation in Python makes the results more reliable by preventing unsupported customer names, off-menu items, and incorrect totals from being accepted without checking.

**Note:** The test cases above describe what should happen. After running the program, I will record the actual results and any errors found.
