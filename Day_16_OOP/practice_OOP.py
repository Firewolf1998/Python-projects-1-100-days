from prettytable import PrettyTable

table = PrettyTable()

# changing the method
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Carmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Changing the attribute
print(table.align)
table.align = "l"

#print the table
print(table)
