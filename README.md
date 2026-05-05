# 🎯 Hangman Game — Python Console Project

A simple text-based Hangman game built in Python where the player guesses a hidden word one letter at a time. Built as a beginner Python project to practise core programming concepts.

---

## 🎮 Demo

```
===================================
       Welcome to Hangman!
===================================
The word has 6 letters. Good luck!

Word:     _ _ _ _ _ _
Wrong:    0/6
Guessed:  None
-----------------------------------
Guess a letter: r

✅ 'r' is in the word!

Word:     r _ _ _ _ _
Wrong:    0/6  
Guessed:  r
-----------------------------------
Guess a letter: z

❌ 'z' is NOT in the word. 5 chance(s) left.

Word:     r _ _ _ _ _
Wrong:    1/6  ❌
Guessed:  r, z
-----------------------------------
Guess a letter: 
```

---

## ✨ Features

- Random word selection from a built-in word list — different word every run
- Tracks correct and incorrect guesses separately
- Displays guessed letters so the player never repeats accidentally
- Input validation — rejects numbers, symbols, and multi-character input
- Clear win/lose message at the end revealing the secret word
- Beginner-friendly code with detailed comments throughout

---

## 🧠 Concepts Covered

| Concept | Where it's used |
|---|---|
| `import random` | Picking a random word each run |
| `while` loop | Keeping the game running until win or lose |
| `if / elif / else` | Checking guesses, validating input |
| Lists | Storing the word bank, display blanks, and guessed letters |
| Strings | Comparing letters, `.lower()`, `.strip()`, `.isalpha()` |
| `enumerate()` | Revealing the correct position of a guessed letter |
| `random.seed()` | Ensuring true randomness on every run |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine
- No external libraries needed — uses only the built-in `random` module

### Run the game

```bash
# Clone the repository
git clone https://github.com/your-username/hangman-python.git

# Navigate into the project folder
cd hangman-python

# Run the game
python hangman.py
```

---

## 📁 Project Structure

```
hangman-python/
│
└── hangman.py       # Main game file — all logic lives here
└── README.md        # You are here
```

---

## 🕹️ How to Play

1. Run the program — a secret word is chosen randomly
2. You are shown blank dashes representing each letter of the word
3. Type one letter at a time and press Enter
4. If the letter is in the word, it gets revealed in its correct position(s)
5. If the letter is wrong, your wrong guess counter goes up by 1
6. You have **6 wrong guesses** before the game ends
7. Guess all letters before running out of chances to win!

---

## ⚙️ Configuration

You can easily customise the game by editing `hangman.py`:

**Change the word list** — add or remove words from this line:
```python
word_list = ["python", "banana", "jungle", "rocket", "castle"]
```

**Change the number of allowed wrong guesses:**
```python
max_wrong = 6   # increase for easier, decrease for harder
```

---

## 📚 What I Learned

This project was built as part of learning Python fundamentals. Key takeaways:

- How to use `random.choice()` and `random.seed()` for unpredictable results
- How `while` loops keep a program running based on game state
- How lists can act as a mutable display (updating `_` to revealed letters)
- How `enumerate()` lets you loop with both index and value at once
- How input validation makes programs more robust and user-friendly

---

## 🔮 Possible Future Improvements

- Add ASCII art of the hangman that draws progressively with each wrong guess
- Load words from an external `.txt` file for a larger word bank
- Add difficulty levels (easy = 8 guesses, hard = 4 guesses)
- Add a hint system that reveals one letter if the player is stuck
- Build a GUI version using `tkinter`

---

## 👤 Author

**Alex Johnson**
- GitHub: [@alexjohnson](https://github.com/alexjohnson)
- LinkedIn: [linkedin.com/in/alexjohnson](https://www.linkedin.com/in/alexjohnson)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
