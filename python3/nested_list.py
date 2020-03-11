############################ my code ################################

students = list()

number_of_students = int(input())

for i in range(number_of_students):
    name = input()
    score = float(input())
    students.append([name, score])

scores = set([students[x][1] for x in range(number_of_students)])
scores = list(scores)
scores.sort()

students = [k[0] for k in students if k[1] == scores[1]]
students.sort()

for i in students:
    print(i)

####################### end of my code ############################