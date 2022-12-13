MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def ifreport(money):
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f"Money: ${money}")


def check_drink(drink):
    for contains in MENU[drink]['ingredients']:
        if resources[contains] < MENU[drink]['ingredients'][contains]:
            print(f"Sorry there is not enough {contains}.")
            return False
        else:
          return True

def coins(drink):
    print("Please insert coins")
    quaters = int(input("how many quaters? "))
    dimes = int(input("how many dimes? "))
    nickels = int(input("how many nickels? "))
    pennies = int(input("how many pennies? "))
    total = (0.25*quaters)+(0.10*dimes)+(0.05*nickels)+(0.01*pennies)
    if total >= MENU[drink]['cost']:
      change = round(total - MENU[drink]['cost'], 2)
      print(f"Here is ${change} change")
      return True
    else:
      print("Sorry that's not enough money. Money refunded.")
      return False
      
def reflected(drink, resources):
  for contains in MENU[drink]['ingredients']:
    resources[contains] -= MENU[drink]['ingredients'][contains]
  return resources
    

money = 0
maintenance = True
while maintenance:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == "report":
        ifreport(money)
    elif drink == "off":
        maintenance = False
    elif check_drink(drink):
        if coins(drink):
          resources = reflected(drink,resources)
          money += MENU[drink]['cost']
          print(f"Here is your {drink}, Enjoy!!!")
        
      
    