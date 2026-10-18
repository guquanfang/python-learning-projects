# GitHub Profile Inspector

A small Python learning project created while studying **Libraries, APIs, JSON, and command-line arguments**.

## Learning Source

This project was created while following the **CS50's Introduction to Programming with Python (CS50P)** course.

Course:
- CS50P — Introduction to Programming with Python
- Lecture 4: Libraries
- Course website: https://cs50.harvard.edu/python/
- Lecture video: https://youtu.be/MztLZWibctI

## Project Goal

The goal of this project is to practice using Python libraries, command-line arguments, APIs, JSON data, and custom modules by retrieving public GitHub user information.

## Features

The program can:

- Accept a GitHub username from the command line
- Request public profile data from the GitHub API
- Display basic user information
- Display the user's first 5 public repositories
- Handle missing command-line arguments
- Handle invalid or nonexistent GitHub usernames

## Project Structure

```text
github-profile-inspector/
├── main.py
├── github_api.py
├── requirements.txt
└── README.md
```

## Installation

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Usage

Run the program with a GitHub username:

```bash
python main.py octocat
```

Example output:

```text
Username: octocat
ID: 583231
Followers: ...

===== Repositories =====
1. repository-name
2. repository-name
3. repository-name
4. repository-name
5. repository-name
```

## How It Works

The program uses:

- `sys.argv` to read the GitHub username from the command line
- `requests` to send requests to the GitHub API
- `response.json()` to convert JSON responses into Python data
- Lists and dictionaries to access returned data
- List slicing to display only the first 5 repositories
- A custom `github_api.py` module to separate API logic from the main program

## What I Learned

In this project, I practiced:

- Importing Python modules
- Installing and using third-party packages
- Using `sys.argv`
- Working with command-line arguments
- Making HTTP requests with `requests`
- Working with APIs
- Reading JSON data
- Working with lists and dictionaries
- Using list slicing
- Returning values from functions
- Using `None` to represent failed results
- Creating and importing custom Python modules
- Using `main()`
- Using `if __name__ == "__main__":`
- Organizing a small multi-file Python project
- Using `requirements.txt`

## Learning Notes

This is a learning project rather than a production-ready GitHub client.

Its purpose is to help me understand how Python programs can use external libraries, communicate with web APIs, process returned data, and organize code across multiple files.
