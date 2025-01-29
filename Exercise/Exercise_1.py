# need to pip install nltk

import nltk
nltk.download('words')

from nltk.corpus import words
import random
import time

# Load the list of words
list_of_words = words.words()

# Select a random word
random_word = random.choice(list_of_words).lower()

# Create a set of letters in the random word for comparison
letters_in_word = set(random_word)

# Create a set for guessed letters
guessed_letters = set()

# Hangman progress (0 means no hangman image, 7 means fully drawn)
progress = 0

# Number of allowed incorrect guesses
max_incorrect_guesses = 7

def print_hangman_image(progress):
    hangman_images = [
        '''
        +---+
            |
            |
            |
            |
            |
        =======
        ''',
        '''
        +---+
        |   |
            |
            |
            |
            |
        =======
        ''',
        '''
        +---+
        |   |
        |   O
            |
            |
            |
        =======
        ''',
        '''
        +---+
        |   |
        |   O
        |   |
            |
            |
        =======
        ''',
        '''
        +---+
        |   |
        |   O
        |   | |
            |
            |
        =======
        ''',
        '''
        +---+
        |   |
        |   O
        |   | |
        |   |
            |
        =======
        ''',
        '''
        +---+
        |   |
        |   O
        |   | |
        |  /|
            |
        =======
        ''',
        '''
        +---+
        |   |
        |   O
        |   | |
        |  /|\\
        |  / \\
        =======
        '''
    ]
    print(hangman_images[progress])

def display_word():
    display = ''.join([letter if letter in guessed_letters else '_' for letter in random_word])
    print("\nWord to guess:", ' '.join(display))

def clear_screen():
    print("\033[H\033[J", end="")  # Clears the screen for a clean look.

# Game loop
clear_screen()
print("Welcome to Hangman!")
print("Try to guess the word before you run out of attempts.\n")
while progress < max_incorrect_guesses:
    display_word()
    print_hangman_image(progress)
    
    # Ask the user for a letter
    guess = input("\nEnter a letter: ").lower()
    
    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("\nInvalid input! Please enter a single letter.")
        time.sleep(1)
        continue
    
    # Check if the letter is in the word
    if guess in guessed_letters:
        print(f"\nYou've already guessed '{guess}'. Try again.")
        time.sleep(1)
        continue
    elif guess in letters_in_word:
        guessed_letters.add(guess)
        print(f"\nGood guess! '{guess}' is in the word.")
    else:
        guessed_letters.add(guess)
        progress += 1
        print(f"\nOops! '{guess}' is not in the word.")
    
    # Check if the user has guessed all the letters
    if all(letter in guessed_letters for letter in random_word):
        display_word()
        print_hangman_image(progress)
        print("\nCongratulations! You've guessed the word!")
        break
    clear_screen()
else:
    display_word()
    print_hangman_image(progress)
    print(f"\nGame Over! The word was '{random_word}'.")
