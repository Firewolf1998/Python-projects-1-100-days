'''
You are going to write a program that calculates the average student height from a List of heights.
'''
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# total_height = sum(student_heights)
# average_height = round(total_height/len(student_heights))
# print(average_height)


total_height=0
for n in range(0, len(student_heights)):
    total_height += student_heights[n]
average_height = round(total_height/len(student_heights))
print(average_height)


