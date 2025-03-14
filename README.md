# Hangman Game with MySQL Integration

## Overview
This is a Python-based Hangman game that integrates with MySQL to store player data, including usernames, email IDs, and scores. The game allows users to create an account, log in, and play a word-guessing game with a hint related to Indian tourist cities.

## Features
- User authentication (account creation and login)
- Random word selection from a predefined list
- Score tracking and updating in a MySQL database
- Command-line interface for gameplay
- Error handling for invalid inputs

## Prerequisites
Before running the game, ensure you have the following installed:
- Python 3
- MySQL Server
- MySQL Connector for Python

## Setup Instructions
### 1. Install Required Libraries
Ensure you have the MySQL connector installed. You can install it using pip:
```sh
pip install mysql-connector-python
```

### 2. Create MySQL Database and Table
Create a MySQL database named `hangman` and a table named `players` using the following SQL commands:
```sql
CREATE DATABASE hangman;

USE hangman;

CREATE TABLE players (
    name VARCHAR(255) PRIMARY KEY,
    email_id VARCHAR(255) UNIQUE,
    points INT DEFAULT 0
);
```

### 3. Configure Database Connection
Update the `host`, `user`, and `password` values in the Python script to match your MySQL credentials:
```python
conn = sql.connect(host="localhost", user="root", password='your_password', database='hangman')
```

### 4. Prepare the Word List
Create a separate Python file named `words.py` and define a list of words:
```python
LIST = ["delhi", "mumbai", "jaipur", "kolkata", "agra"]
```

### 5. Run the Game
Execute the script using:
```sh
python hangman.py
```

## How to Play
1. Choose to create a new account or log in.
2. If creating a new account, enter a name and email ID.
3. If logging in, provide your email ID and password.
4. A random word (Indian tourist city) is selected.
5. Guess letters to complete the word.
6. If you guess correctly, you earn 100 points.
7. Your score is updated in the database.

## Error Handling
- Prevents duplicate letter guesses.
- Ensures only single alphabet characters are entered.
- Handles incorrect inputs gracefully.
- Uses `try-except` for runtime interruptions.

## Future Improvements
- Implement password hashing for secure authentication.
- Enhance the word list with more categories.
- Add a graphical interface for better user experience.
