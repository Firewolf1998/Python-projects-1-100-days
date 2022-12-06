#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
print("Welcome to the guessing game")
print("I am thinking of a number between 1 to 100")
import random

def compare(to_guess, user_no):
  if user_no == to_guess:
    print("Congrats!! You guessed the right number.")
    return True
  if user_no > to_guess:
    print("Too high")
    print("Guess again")
    return False
  if user_no < to_guess:
    print("Too low")
    print("Guess again")
    return False

guess_no = random.randint(0,100)
game_mode = input("Enter the difficulty level. easy or hard ")
if game_mode == "easy":
  tries = 10
elif game_mode == "hard":
  tries = 5
else:
  print("invalid answer")
  end_game = False

end_game = True
while tries > 0 and end_game:
  print(f"You have {tries} number of tries remaining")
  user_no = int(input("Make a guess:  "))
  result = compare(guess_no, user_no)
  if result == True:
    end_game = False
  tries -= 1
  
