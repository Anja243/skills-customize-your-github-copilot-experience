# 📘 Assignment: Games in Python

## 🎯 Objective

Build a Hangman game in Python that uses loops, conditionals, and string operations.
By the end of this assignment, you will create a playable command-line game with clear win and lose outcomes.

## 📝 Tasks

### 🛠️ Build the Core Hangman Game

#### Description
Create the main game loop for Hangman. The program should choose a word, let the player guess one letter at a time, and reveal correctly guessed letters in their positions.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of words.
- Show the current word progress using underscores for unknown letters (for example: `_ _ _ _`).
- Accept one-letter guesses from the player and update the display when guesses are correct.
- Track and display the number of incorrect guesses remaining.
- End the game when the player guesses the full word or runs out of attempts.


### 🛠️ Improve Game Experience

#### Description
Enhance your game so it is easier and more fun to play. Focus on handling common input issues and giving helpful feedback during gameplay.

#### Requirements
Completed program should:

- Prevent duplicate guesses from reducing remaining attempts.
- Validate input so only a single alphabetic character is accepted.
- Show a clear win message when the word is guessed.
- Show a clear lose message that reveals the hidden word.
- Ask the player if they want to play another round.
