def grading (score):
    '''int score and grades depending on the score'''
    if score > 100:
        output = "Score can't be above 100"
    elif score >= 70:
        output = "A"
    elif score >= 60:
        output = "B"
    elif score >= 50:
        output = "C"
    elif score >= 40:
        output = "D"
    else:
        output = "F"
    return output

student_score = list ()
student_name = list ()
student_grade = list ()
size = int(input ("How many students do you want to grade?\n"))
for i in range(size):
    name = input("Please enter student's name\n")
    student_name.append(name)
    score = int(input("Please enter the student's score\n"))
    student_score.append(score)
    grade = grading(score)
    student_grade.append(grade)
print ("\nSN\tStudent's Name\tStudent's Score\tStudent's Grade")
for j in range(size):
    print (j+1, "\t", student_name[j], "\t\t", student_score[j], "\t\t", student_grade[j])
