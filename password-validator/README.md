# Password Validator

A small Python learning project created while studying **Unit Testing with pytest**.

## Learning Source

This project was created while following the **CS50's Introduction to Programming with Python (CS50P)** course.

Course:
- CS50P — Introduction to Programming with Python
- Lecture 5: Unit Tests
- Course website: https://cs50.harvard.edu/python/
- Lecture video: https://youtu.be/tIrcxwLqzjQ

## Project Goal

The goal of this project is to practice writing a password validation function and testing different normal, boundary, and invalid inputs.

## Password Rules

A valid password must:

- Be between 8 and 18 characters long
- Contain at least one uppercase letter
- Contain at least one lowercase letter
- Contain at least one digit

## Project Structure

```text
password-validator/
├── main.py
├── password_validator.py
├── test_password_validator.py
├── requirements.txt
└── README.md
```

## Run the Program

```bash
python main.py
```

## Run the Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
pytest
```

## What I Learned

In this project, I practiced:

- Writing reusable Python functions
- Boolean conditions
- `isupper()`, `islower()`, and `isdigit()`
- Unit testing with `pytest`
- Using `assert`
- Testing edge cases
- Testing exceptions with `pytest.raises()`
- Organizing a small Python project

## Learning Notes

This is a learning project rather than a production-ready password security tool. Its purpose is to help me practice Python testing and program structure.