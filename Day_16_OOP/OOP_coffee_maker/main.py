from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffeemenu = Menu()
coffeemaker = CoffeeMaker()
coffeemachine = MoneyMachine()


should_continue = True
while should_continue:
  option = coffeemenu.get_items()
  order_name = input(f"What would you like? {option}: ")
  if order_name == "off":
    should_continue = False
  elif order_name == "report":
    print(coffeemaker.report())
    print(coffeemachine.report())
  else:
    drink = coffeemenu.find_drink(order_name)
    if coffeemaker.is_resource_sufficient(drink) and coffeemachine.make_payment(drink.cost):
        coffeemaker.make_coffee(drink)
    
  

