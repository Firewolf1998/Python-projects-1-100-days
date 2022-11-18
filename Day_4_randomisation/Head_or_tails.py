#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
'''
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
'''	 
#Write the rest of your code below this line 👇
import random
random_int = random.randint(0,1)
if random_int ==0:
    print("Heads")
else:
    print("Tails")