# word-guess
word-guess is an Python implementation of Wordle.

## Description
Wordle is a word game in which the player has 6 attempts to guess a random 5 letter word. Each letter of the player's guess is assigned a color based on accuracy. Green indicates a letter is in the correct position, yellow indicates a letter is in the wrong position, and grey indicates a letter is not located in any position. If the player has guessed 6 times and has still not guessed correctly, the correct answer is displayed.

word-guess is a straightforward implementation of Wordle written in Python. It features a hand-picked list of over 900 words, a score distribution chart, and a simple desktop user interface.

## Dependencies
* PyQt6
* PyQtGraph

To install these dependencies, run the following command:
```
pip install pyqt6 pyqtgraph
```

## Running
After downloading word-guess, navigate to the project directory and run the following command:
```
python word-guess.py
```

## License
word-guess is licensed under version 3 of the GPL. For more information, see `LICENSE`.
