'''
 A program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
'''
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_no = random.randint(0,len(names)-1)
print(f"{names[random_no]} is going to buy the meal today!")
