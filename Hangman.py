def choose_word():
    word = 'Github'
    return word.lower()

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def guessed_letters():""

def hangman():
    guessed_letters = set()
    attempts_remaining = 5
    while attempts_remaining > 0:
        print("\nWord to guess:", display_word(choose_word(), guessed_letters))
        print("Attempts remaining:", attempts_remaining)
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in choose_word():
            print("Good guess!")
            if all(letter in guessed_letters for letter in choose_word()):
                print("\nCongratulations! You guessed the word:", choose_word())
                break
        else:
            print("Wrong guess.")
            attempts_remaining -= 1
    else:
        print("\nGame over! The word was:", choose_word())

if __name__ == "__main__":
    print("Welcome to Hangman!")
    hangman()
