# Number Guessing Game
A Python-based number guessing game where players attempt to guess a randomly generated number between 1 and 50 within a limited number of attempts.

Unlike a simple guessing game, this project stores player data and statistics across sessions using JSON files.

## Features

- Random number generation
- Hint system ("higher", "lower", and close-range hints)
- User account creation
- Persistent user data using JSON
- Games played tracking
- Wins tracking
- Best score tracking
- Win percentage calculation
- Score history logging
- Input validation and exception handling
- Automatic creation of user data files when needed

## Statistics Tracked

Each user has:

- Games Played
- Wins
- Best Score (fewest guesses needed)
- Win Percentage

## Files Used

### users.json

Stores user profiles and statistics.

### score.txt

Stores a history of successful games and player performances.

## Concepts Practiced

- Loops
- Conditional Statements
- Functions
- Dictionaries
- Nested Dictionaries
- File Handling
- JSON Serialization
- Exception Handling
- Random Number Generation

## Future Improvements

Possible future additions include:

- Leaderboards
- Achievement System
- Average Guess Statistics
- Multiple Difficulty Levels
- Graphical User Interface (GUI)

This project was built as part of my Python learning journey and gradually expanded from a simple guessing game into a persistent statistics-based application.
