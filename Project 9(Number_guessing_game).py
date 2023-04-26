#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo 

def play_game(difficulty):
  if difficulty == "easy":
    max_guess = 10
  elif difficulty == "hard":
    max_guess = 5
  else:
    print("Invalid difficulty level!")

  secret_number = random.randint(1, 100)
  guess_left = max_guess

  while guess_left > 0:
    guess = int(input("Guess a number between 1 to 100: "))
    if guess == secret_number:
      print(f"You guessed it! The secret number was: {secret_number}")
    elif guess < secret_number:
      print("two low")
    elif guess > secret_number:
      print("Tow high")
    guess_left -= 1
    print(f"You have {guess_left} guess left.")

  print(f"Sorry! You ran out of guesses. The secret number is {secret_number}")

print(logo)
difficulty = input("Choose a difficulty level (easy/hard): ")
play_game(difficulty)  