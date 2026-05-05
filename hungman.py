import random

# ── Word bank (5 words) ───────────────────────────────────────────
word_list = ["python", "banana", "jungle", "rocket", "castle"]

# ── Pick a truly random word every run ───────────────────────────
# random.seed() with no argument uses the system clock,
# so you get a different word each time you run the program.
random.seed()
word = random.choice(word_list)

# ── Set up tracking variables ─────────────────────────────────────
display        = ["_"] * len(word)   # e.g. ["_","_","_","_","_","_"]
guessed_letters = []
wrong_guesses  = 0
max_wrong      = 6

print("=" * 35)
print("       Welcome to Hangman!")
print("=" * 35)
print(f"The word has {len(word)} letters. Good luck!\n")

# ── Main game loop ────────────────────────────────────────────────
while wrong_guesses < max_wrong and "_" in display:

    print("Word:    ", " ".join(display))
    print(f"Wrong:    {wrong_guesses}/{max_wrong}  {'❌' * wrong_guesses}")
    print("Guessed: ", ", ".join(guessed_letters) if guessed_letters else "None")
    print("-" * 35)

    guess = input("Guess a letter: ").strip().lower()

    # ── Input validation ──────────────────────────────────────────
    if len(guess) != 1 or not guess.isalpha():
        print("⚠  Please enter ONE letter only.\n")
        continue

    if guess in guessed_letters:
        print(f"⚠  You already guessed '{guess}'. Try another letter.\n")
        continue

    # ── Record the guess ──────────────────────────────────────────
    guessed_letters.append(guess)

    # ── Check if correct ─────────────────────────────────────────
    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                display[index] = guess
        print(f"✅ '{guess}' is in the word!\n")
    else:
        wrong_guesses += 1
        remaining = max_wrong - wrong_guesses
        print(f"❌ '{guess}' is NOT in the word. {remaining} chance(s) left.\n")

# ── Game over ─────────────────────────────────────────────────────
print("\n" + "=" * 35)
if "_" not in display:
    print(f"🎉 YOU WIN!  The word was: {word.upper()}")
else:
    print(f"💀 GAME OVER! The word was: {word.upper()}")
print("=" * 35)