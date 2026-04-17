import random

def hangman():
    words = ["python", "data", "science", "hangman", "project"]
    word = random.choice(words)

    guessed = ["_"] * len(word)
    attempts = 6
    used_letters = set()

    print("Hangman Game")

    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        print("Attempts left:", attempts)

        guess = input("Guess a letter: ").lower()

        if guess in used_letters:
            print("You already tried that letter.")
            continue

        used_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Correct!")
        else:
            attempts -= 1
            print("Wrong guess!")

    if "_" not in guessed:
        print("\nYou win! The word was:", word)
    else:
        print("\nGame over! The word was:", word)


if __name__ == "__main__":
    hangman()
