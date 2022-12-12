from game_data import data
import random
import art
from replit import clear

def compare(data1,data2):
  data1_count = data1["follower_count"]
  data2_count = data2["follower_count"]
  if data1_count > data2_count:
    return "A"
  else:
    return "B"
  
score = 0
got_wrong = False

random1= random.randint(0,len(data)-1)
random2= random.randint(0,len(data)-1)

if random1 != random2:
  data1 = data[random1]
  data2 = data[random2]
print(art.logo)  
while not got_wrong:
  print( "Compare A " + data1["name"]+ ", a "+ data1["description"] + " , from "+ data1["country"])
  print(art.vs)
  print("Against B " + data2["name"]+ ", a "+ data2["description"] + " , from "+ data2["country"])
  user_input = input("Which is higher, A or B:  ")
  compare_results = compare(data1, data2)
  
  if user_input == compare_results:
    clear()
    print(art.logo)
    score +=1
    print(f"That is Right!! Current score = {score}")
    data1 = data2
    data2 = data[random.randint(0,len(data)-1)]
  else:
    clear()
    print(art.logo)
    print(f"Sorry, That is Wrong!! Final score = {score}")
    got_wrong = True