
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman game in Python where players guess letters to reveal a hidden word before running out of attempts. Practice string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️	Implement Game Logic

#### Description
Create the core Hangman game functionality that allows a player to guess letters and reveals the hidden word progressively. The game should track correct and incorrect guesses and provide feedback to the player.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of words
- Display the word as underscores for unguessed letters (e.g., _ _ _ _)
- Accept single-letter guesses from the user
- Show current progress after each guess
- Track and display the number of incorrect guesses remaining
- End the game with a win message when the word is completely guessed
- End the game with a lose message when attempts are exhausted


### 🛠️	Add Game Enhancements

#### Description
Enhance your Hangman game with additional features to improve the user experience and add replay functionality.

#### Requirements
Completed program should:

- Ask the player if they want to play again after each game ends
- Start a new game with a fresh word when the player chooses to continue
- Display a list of previously guessed letters during gameplay
- Validate input to ensure only single letters are accepted
- Handle duplicate guesses appropriately (inform user but don't penalize)
