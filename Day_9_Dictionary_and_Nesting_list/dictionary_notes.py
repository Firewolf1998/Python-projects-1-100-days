programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."} # {key:value}

# Retrieving data from dictionaries
# print(programming_dictionary["Bug"])

# Adding data to dictionaries
programming_dictionary["key_name"] = "value_name "
# print(programming_dictionary)

# Creating empty dictionaries
empty_dictionary = {}

# wipe entire dictionary
# programming_dictionary = {}

# Edit items in dictionary
programming_dictionary["Bug"] = "A moth in your code"
# print(programming_dictionary)

# Loop through a list
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])