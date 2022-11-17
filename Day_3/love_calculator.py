'''
To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.
'''
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
combo_name = name1+name2


t = combo_name.count("t")
r = combo_name.count("r")
u = combo_name.count("u")
e = combo_name.count("e")
true = t+r+u+e

l = combo_name.count("l")
o = combo_name.count("o")
v = combo_name.count("v")
e = combo_name.count("e")
love = l+o+v+e

score = int(str(true) + str(love))
# score = true*10+love
if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")