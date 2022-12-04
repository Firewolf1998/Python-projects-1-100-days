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
n1 = int(input("What is your First no."))
for symbol in operation:
  print(symbol)
operation_value = input("What operation do you choose from above")
n2 = int(input("What is your Second no."))
calculation_function = operation[operation_value]
answer = calculation_function(n1,n2)
print(f"{n1} {operation_value} {n2} = {answer}")
