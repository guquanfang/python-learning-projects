# Personal Wealth Tracker — Project Context

## 1. Project Goal

I am building a personal wealth tracking tool while learning Python.

The goal is not only to make the program work, but also to understand the code and gradually improve my programming ability.

This project may later grow into a more complete personal finance dashboard.

---

## 2. Current Python Level

I currently understand the basics of:

- Variables
- `if` statements
- `for` loops
- `while True`
- Lists
- Dictionaries
- Functions
- `return`
- Basic user input
- Basic input validation
- `try/except`

I am still a beginner, so avoid unnecessarily advanced syntax unless it is explained first.

---

## 3. Current Project Version

Current version: `v0.3`

Current goal:

1. Let the user enter:
   - cash
   - bank balance
   - long-term investment
   - trading account balance

2. Store the values in an `assets` dictionary.

3. Calculate total assets using:

```python
sum(assets.values())
```

4. Calculate the percentage of total assets represented by each category.

5. Display the result clearly.

Example:

```text
cash: ¥2000 - 8.70%
bank: ¥5000 - 21.74%
long_term_investment: ¥0 - 0.00%
trading_account: ¥16000 - 69.57%

Total Assets: ¥23000
```

---

## 4. Planned Development

Possible future versions:

### v0.1
Basic asset tracker.

### v0.2
Add input validation.

### v0.3
Save data locally using JSON or CSV.

### v0.4
Track monthly income and expenses.

### v0.5
Calculate savings rate and cash flow.

### v0.6
Track net worth over time.

### v0.7
Add charts.

### v0.8
Create a Streamlit web interface.

### v0.9
Add asset allocation analysis.

### v1.0
Build a usable personal wealth dashboard.

Possible future features:

- Compound interest calculator
- Long-term investment account tracking
- Trading account tracking
- Net worth history
- Monthly spending categories
- CSV import
- Wealth simulation
- Financial goal tracking

---

## 5. AI Coding Rules

When helping me with this project:

1. Do not rewrite the entire project unless necessary.

2. Make one small change at a time.

3. Preserve my existing code structure whenever possible.

4. Prefer giving hints before giving the complete solution when the task is something I can reasonably write myself.

5. If you modify my code, explain:
   - what was changed
   - why it was changed
   - what Python concept is involved

6. Avoid advanced syntax unless:
   - it provides a clear benefit
   - you explain it first

7. Do not introduce many new libraries at once.

8. If my code works but can be improved, first explain the problem before refactoring it.

9. Treat this as both a real software project and a Python learning project.

10. The goal is for me to eventually be able to explain the important parts of the code myself.

---

## 6. Development Philosophy

Use AI as a coding assistant, not as a replacement for learning.

The workflow should usually be:

Idea → small feature → write code → test → debug → understand → improve → commit

Each version should remain understandable and runnable.

The project should gradually become more useful as my Python skills improve.