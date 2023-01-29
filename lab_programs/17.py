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
    answerKey = f.readline().strip().split(' ')[1:]
    # answerKey.pop(0)

students = {}
with open(fileName, 'r') as f:
    for line in f:
        x = line.strip().split(' ')
        students[x[0]] = x[1:]

# import itertools
# studentMarks = {student: sum(ans == key for ans, key in zip(
#     students[student], answerKey)) for student in students.keys()}

studentMarks = {}
for name in students.keys():
    marks = sum(answerKey[i] == students[name][i]
                for i in range(len(answerKey)))
    studentMarks[name] = marks
    print(name, ":", marks)

topScore = max(studentMarks.values())
topScorer = [name for name in studentMarks if studentMarks[name] == topScore]

print("Top Score =", topScore)
for student in topScorer:
    print("Top Scorer :", student)
