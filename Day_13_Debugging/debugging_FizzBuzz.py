for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: # should be and not or
    print("FizzBuzz")
  elif number % 3 == 0: #should be elif not if
    print("Fizz")
  elif number % 5 == 0: #should be elif not if
    print("Buzz")
  else:                 
    print(number)       #should be number not [number]
