import requests
import random
from ascii_art import stages
from cipher_caesar import *

response = requests.get("https://random-word-api.vercel.app/api?words=10") # API
data = response.json()

test_data = data
shift = 2

chosen_word = encrypt(random.choice(test_data), shift)

game_over = False
lives = 7
placeholder = ''

for letter in chosen_word:
    placeholder += "_"

correct_letters = []

print(f"placeholder" + placeholder)
while not game_over:
    display = ''

    print(stages[lives])
    print(f"YOUR LIVES: ({lives})\nWORD LEN ({len(chosen_word)})")
    guess = input("guess a letter: ").lower()

    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'


    print(f"\n\ndisplay: {display}")

    if guess not in chosen_word:
        lives -= 1
        if lives < 0:
            game_over = True
            print(f"You lose! The original word: {decrypt(chosen_word, shift)}")

    if "_" not in display:
        game_over = True
        print(f"You Win! The original word: {decrypt(chosen_word, shift)}")
