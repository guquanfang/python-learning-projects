# Python Basic Exercises

A collection of small Python exercises created during the early stages of my Python learning journey.

These exercises mainly cover the fundamental concepts introduced in the first few lectures of **CS50's Introduction to Programming with Python (CS50P)**.

## Learning Source

Course:

- CS50P — Introduction to Programming with Python
- Course website: https://cs50.harvard.edu/python/
- YouTube course playlist: CS50's Introduction to Programming with Python

The exercises in this folder mainly correspond to the early topics of the course, including:

- Functions and Variables
- Conditionals
- Loops
- Basic Exception Handling

## Topics Practiced

### Functions and Variables

I practiced:

- Defining functions with `def`
- Passing arguments into functions
- Returning values with `return`
- Using variables
- Working with strings, integers, and floating-point numbers
- Using `input()` and `print()`
- Formatting output with f-strings

Example concepts:

```python
def greet(name):
    return f"Hello, {name}"
```

### Conditionals

I practiced controlling program behavior using:

- `if`
- `elif`
- `else`
- Comparison operators
- Boolean expressions
- `and`, `or`, and `not`

Example:

```python
if score >= 60:
    print("Pass")
else:
    print("Fail")
```

### Loops

I practiced repeating operations using:

- `for`
- `while`
- `range()`
- `break`
- Looping through lists and dictionaries
- Using `while True`
- Understanding how `return` can end a function

Example:

```python
for item in items:
    print(item)
```

### Lists and Dictionaries

I practiced storing and organizing data using:

- Lists
- Dictionaries
- `append()`
- Accessing dictionary values using keys
- Lists containing dictionaries

Example:

```python
task = {
    "name": "Python",
    "time": 2
}
```

### Basic Exception Handling

I also started learning how programs can handle invalid input using:

- `try`
- `except`
- `ValueError`

This helped me understand how to prevent programs from crashing when the user enters unexpected data.

## Exercises

This folder contains small programs and exercises used to practice individual Python concepts.

Some exercises focus on only one concept, while others combine:

- Functions
- Loops
- User input
- Lists
- Dictionaries
- Basic data processing

These exercises are mainly intended for practice rather than production use.

## What I Learned

Through these exercises, I gradually learned how to:

- Break a problem into smaller steps
- Store information using variables and data structures
- Control program flow
- Repeat operations with loops
- Organize code into functions
- Pass data between functions using parameters and return values
- Read and modify lists and dictionaries
- Handle simple user-input errors
- Debug basic Python programs

## Learning Notes

This folder represents the early stage of my Python learning.

Later projects in this repository build on these fundamentals and introduce topics such as:

- Libraries
- APIs
- JSON
- Command-line arguments
- Unit testing with `pytest`
- Multi-file Python projects