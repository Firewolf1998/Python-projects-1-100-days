"""
You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
"""



#Write your code below this row 👇
total_even = 0
for n in range(2,101,2):
    total_even += n
print(total_even)

total2 = 0
for n in range (0,101):
    if n%2 == 0:
        total2 +=n
print(total2)