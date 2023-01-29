# Develop python program to perform the below mentioned operations.

# a) display total marks scored by each student
# b) Display top scorer and the top score

# Scenario: There are 8 students and answers to 10 multiple
# choice questions of each student is stored in a file
# called marks.txt. Each answer is delimited by space. Each
# line provides a student’s answers to the questions, as
# shown below.The answer key isstored in a file named keys.txt.
# The format of answer keys as shown below.

# Key D B D C C D A E A D
# Student0 A B A C C D E E A D
# Student1 D B A B C A E E A D
# Student2 E D D A C B E E A D
# Student3 C B A E D C E E A D
# Student4 A B D C C D E E A D
# Student5 B B E C C D E E A D
# Student6 B B A C C D E E A D
# Student7 E B E C C D E E A D

fileName = 'marks.txt'
keyFileName = 'key.txt'

with open(keyFileName, 'r') as f:
    keyFile = f.readline()

with open(fileName, 'r') as f:
    file = f.readlines()

answerKey = [i for i in keyFile.split(
    ' ') if i.isalnum() and len(i) == 1]

students = {}
for student in file:
    student = student.split(' ')
    students[student[0]] = [i for i in student if i.isalnum() and len(i) == 1]

studentMarks = {}
max = 0
for student in students.keys():
    score = 0
    for i in range(len(answerKey)):
        if answerKey[i] == students[student][i]:
            score += 1
    studentMarks[student] = score
    max = score if max < score else max

topScorer = []
for student in studentMarks.keys():
    marks = studentMarks[student]
    print(student, "marks =", marks)
    if marks == max:
        topScorer.append(student)

print("Top Score =", max)
for student in topScorer:
    print("Top Scorer :", student)
