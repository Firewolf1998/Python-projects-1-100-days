'''
Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. 
The final version of the student_grades dictionary will be checked.
This is the scoring criteria:
Scores 91 - 100: Grade = "Outstanding"
Scores 81 - 90: Grade = "Exceeds Expectations"
Scores 71 - 80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Fail"
'''
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student_name in student_scores:
    if student_scores[student_name]>=91:
        student_grades[student_name] = "Outstanding"
    elif student_scores[student_name]>=81 and student_scores[student_name] <=90: 
        student_grades[student_name] =  "Exceeds Expectations"
    elif student_scores[student_name]>=71 and student_scores[student_name] <=80: 
        student_grades[student_name] = "Acceptable"
    else:
        student_grades[student_name] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)
