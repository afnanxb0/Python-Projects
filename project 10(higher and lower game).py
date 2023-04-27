from HL_game_data import data
import random
#from replit import clear 
from art_H_L import logo, vs
print(logo)




def play_game():
  # Function to generate a random account from the game data
  def get_random_account():
      return random.choice(data)
  
  # Function to format account data into printable format
  def format_account(account):
      return f"{account['name']}, {account['description']} {account['country']}"
  
  #alternative
  # def format_data(account):
  #   name = account["name"]
  #   description = account["description"]
  #   country = account["country"]
  #   #print(f'{name}: {account["follower_count"]}')
  #   return f"{name}, a {description}, from {country}"
  
  # Function to play the game
  # Main game loop
  
  game_over = False
  score = 0
  account_a = get_random_account()
    
  while not game_over:
      account_b = get_random_account()
    
        # Ensure account A and B are different
      while account_b == account_a:
          account_b = get_random_account()
    
      print(f"Compare A: {format_account(account_a)}")
      print(vs)
      print(f"Against B: {format_account(account_b)}")
    
      # Ask user for a guess
      user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    
      # Check if user is correct and give feedback
      if user_guess == "A":
          if account_a["follower_count"] > account_b["follower_count"]:
              print("You're right!")
              score += 1
          else:
              print("Sorry, that's wrong.")
              game_over = True
      elif user_guess == "B":
          if account_b["follower_count"] > account_a["follower_count"]:
              print("You're right!")
              score += 1
          else:
              print("Sorry, that's wrong.")
              game_over = True
      else:
          print("Invalid input. Please enter 'A' or 'B'.")
    
      # Clear the screen
      #input("Press Enter to continue...")
      #clear()
    
      # Make account B become the next account A
      account_a = account_b
    
  # Game over, show final score
  print(f"Game over! Your final score is {score}.")
  
play_game()




# Ask if the player wants to play again
while True:
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() == "y":
        play_game()
    elif play_again.lower() == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

