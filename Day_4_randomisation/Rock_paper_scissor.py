rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game = [rock, paper, scissors]
comp_choice = random.randint(0,2)
your_choice = int(input("What do you choose? 0=Rock, 1=Paper, 2=Scissors   "))
print(f"Your choice:\n {game[your_choice]} \nComputer choice:\n {game[comp_choice]}\n")
if (your_choice==1 and comp_choice==0) or (your_choice==0 and comp_choice==2) or (your_choice==2 and comp_choice==1):
  print ("You Won")
elif (your_choice == comp_choice):
  print("Its a Draw")
else:
  print("You Lose")