# Learning Progress Tracker

A simple command-line learning tracker built with Python.

This project was created during my process of learning Python. Its main purpose is to practice **File I/O**, CSV data storage, exception handling, dictionaries, sorting, and basic testing with `pytest`.

It is not intended to be a complex or production-ready application. I built it as a learning project to understand how a Python program can save data permanently instead of losing everything after the program exits.

## Features

The program currently supports:

- Add a learning record
- View all learning records
- Calculate total study time
- Find the longest study session
- Sort learning records by duration
- Save records permanently in a CSV file
- Validate invalid duration input
- Handle missing CSV files
- Basic automated testing with `pytest`

## Project Structure

```text
learning-progress-tracker/
│
├── main.py
├── records.py
├── test_record.py
├── learning_records.csv
└── README.md
```

### `main.py`

Contains the main menu and controls the interaction between the user and the different functions.

### `records.py`

Contains the main program logic, including:

- adding records
- reading CSV data
- calculating total study time
- finding the longest study session
- sorting records by duration

### `test_record.py`

Contains several basic tests written with `pytest`.

The current tests check:

- whether a learning record can be written correctly to a CSV file
- whether the program handles a missing CSV file correctly

## Example

When the program starts:

```text
=== Learning Progress Tracker ===

1.Add learning record
2.View all records
3.View total study time
4.View longest study session
5.Sort records by duration
0.exit
```

A learning record contains:

```text
Date
Topic
Duration
Resource
```

For example:

```text
Date: 2026-10-26
Topic: Python File I/O
Duration(hours): 1.5
Resource: CS50P
```

The data is stored in:

```text
learning_records.csv
```

Example CSV data:

```csv
Date,Topic,Duration,Resource
2026-10-26,Python File I/O,1.5,CS50P
```

## Concepts Practiced

This project helped me practice and connect several Python concepts that I had previously learned separately:

- Functions
- `while` loops
- Conditional statements
- `try` / `except`
- File I/O
- `with open()`
- CSV files
- `csv.DictReader`
- `csv.DictWriter`
- Dictionaries
- Lists
- `lambda`
- `max()`
- `sorted()`
- Modules
- Input validation
- Basic testing with `pytest`

One of the most important things I learned from this project is the difference between temporary data stored in variables and persistent data stored in files.

Before learning File I/O, most of my programs lost their data when they stopped running. In this project, learning records can be stored in a CSV file and loaded again later.

## Running the Program

Run:

```bash
python main.py
```

## Running the Tests

Normally, pytest can be run with:

```bash
pytest
```

On my current Windows environment, I encountered an issue when running pytest directly.

The command that works for me is:

```bash
python -m pytest -q test_record.py --basetemp=.\.pytest-temp-local
```

This may not be necessary on other systems.

## Learning Resource

This project was mainly created while studying:

**Harvard CS50's Introduction to Programming with Python — Week 6: File I/O**

Course:

https://cs50.harvard.edu/python/

YouTube lecture:

https://youtu.be/KD-Yoel6EVQ

## Why I Made This

I am still learning Python, so the projects in this repository are not meant to demonstrate advanced programming skills.

I use these projects to record my learning process, practice concepts by building something myself, and gradually improve my programming ability.

I also hope these small projects can provide some ideas or references for other beginners who are learning Python.

If you are also learning Python, feel free to use this project as a simple practice example.

## Possible Future Improvements

Some possible improvements include:

- Search records by topic
- Filter records by date
- Edit existing records
- Delete records
- Show weekly or monthly study statistics
- Add more automated tests
- Create a graphical interface
- Visualize learning time with charts

This project will continue to improve as I learn more Python.