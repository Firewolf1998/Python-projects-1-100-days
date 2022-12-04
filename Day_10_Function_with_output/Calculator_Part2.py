def add(n1, n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

from art import logo
print(logo)
operation = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  }
def calculator():
  n1 = float(input("What is your First no."))
  should_continue = True
  while should_continue:
    operation_value = input("Pick and operation ")
    n2 = float(input("What is your next no. "))
    calculation_function = operation[operation_value]
    answer = calculation_function(n1,n2)
    print(f"{n1} {operation_value} {n2} = {answer}")
    continue1 = input(f"Type y to continue with {answer} or type n to exit: ")
    if continue1 == "y":
      n1 = answer
    else:
      should_continue = False
      calculator()

calculator()
  
