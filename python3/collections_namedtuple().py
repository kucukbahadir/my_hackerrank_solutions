############################## my code #############################
from collections import namedtuple

number_of_students = int(input())

student = namedtuple("student",input())
student_list = []

for _ in range(number_of_students):
    student_input = input().split()
    
    student_list.append(student(student_input[0], student_input[1], student_input[2],student_input[3]))

total_points = 0 

for i in student_list:
    total_points += int(i.MARKS)

average = total_points / number_of_students
print(average)
########################### end of my code #######################