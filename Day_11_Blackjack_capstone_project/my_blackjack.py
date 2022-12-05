############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  return random.choice(cards)

def calculate_score(card):
  if len(card)==2 and sum(card)==21:
    return 21
  if sum(card)>21 and 11 in card:
    card.remove(11)
    card.append(1)
  return sum(card) 




 

def compare(user_cards, computer_cards):
  if calculate_score(user_cards)==21:
    print("You won")
  elif calculate_score(computer_cards) == 21 or calculate_score(user_cards)>21:
    print("You loose")
  elif calculate_score(computer_cards)>21:
    print("you won, the oponent went over")
  elif calculate_score(user_cards)==calculate_score(computer_cards):
    print("draw")
  elif calculate_score(user_cards)>calculate_score(computer_cards):
    
    print("You Won!!")
  else:
    
    print("You lost")




def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  for card in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  game_end = False
  while not game_end:
    print(f"   Your cards: {user_cards}, current score {calculate_score(user_cards)}")
    print(f"   Computer's first card: {computer_cards[0]}\n")
    if calculate_score(user_cards)==21 or calculate_score(computer_cards) == 0 or calculate_score(user_cards)>21:
      game_end =True
    else:
      another_card = input("Do you need to draw another card? y or n: ")
      if another_card == "y":
        user_cards.append(deal_card())
      else:
        game_end= True
      
  
  while calculate_score(computer_cards)!=21 and calculate_score(computer_cards)<17:
    computer_cards.append(deal_card())
    
  print(f"\nYour cards = {user_cards}, Your final score = {calculate_score(user_cards)},\nComputer cards = {computer_cards}, Computer final score = {calculate_score(computer_cards)} \n")  
  compare(user_cards, computer_cards)      
new_game = True
while new_game:
  game = input("Do you want to play Blackjack? y or n ")
  if game == "y":
    clear()
    play_game()
  else:
    new_game= False
    clear()