from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)

def find_highest_bidder(auction):
  highest_bidder = ""
  highest_bid = 0
  for name in auction:
    if auction[name] > highest_bid:
      highest_bid = auction[name]
      highest_bidder = name
  print(f"The hightest bidder is {highest_bidder}")
    
another_bid = True
auction = {}
while another_bid:
  name = input("What is your name? ")
  bid = int(input("What is your bid? "))
  auction[name]= bid
  bidders_exist = input("Are there any other bidder? yes or no  ")
  if bidders_exist == "no":
    another_bid = False
    find_highest_bidder(auction)
  if bidders_exist == "yes":
    clear()

