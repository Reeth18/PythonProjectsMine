import random

# List of six-letter words
words = ["energy", "friend", "planet", "future", "author", "rocket", "temple", "sunset", "forest", "rescue"]

# Select a random word from the list
secret_word = random.choice(words)

# Get the positions of vowels in the secret word
vowel_positions = [i for i in range(len(secret_word)) if secret_word[i] in "aeiou"]

# Initialize the pattern to be displayed
pattern = ["_" if i not in vowel_positions else secret_word[i] for i in range(len(secret_word))]

# Number of guesses remaining
guesses_remaining = 5

# Play the game until the guesser wins or loses
while guesses_remaining > 0:
    # Display the pattern and the number of guesses remaining
    print(" ".join(pattern))
    print(f"You have {guesses_remaining} guesses remaining")

    # Ask the guesser to guess a consonant
    guess = input("Guess a consonant: ").lower()

    # Check if the guess is correct
    if guess in secret_word and guess not in "aeiou":
        # Update the pattern with the correct guess
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                pattern[i] = guess
        # Check if the guesser has won
        if "_" not in pattern:
            print(" ".join(pattern))
            print("Congratulations! You won the game!")
            break
    else:
        # Reduce the number of guesses remaining
        guesses_remaining -= 1

# If the guesser has used up all their guesses, display the secret word
if guesses_remaining == 0:
    print("Oops! You lost all your chances to guess the letters.!")
    print(f"The word is {secret_word}")
