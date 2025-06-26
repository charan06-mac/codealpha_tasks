import random

def hangman():
    words = ["apple", "chair", "robot", "green", "plant"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    
    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        print("Attempts left:", attempts)
        print("Guessed letters:", " ".join(guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            print("Wrong guess!")
            attempts -= 1

    if "_" not in guessed:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nYou lost! The word was:", word)

# Run the game
hangman()
