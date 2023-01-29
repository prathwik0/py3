fileName = 'marks.txt'
keyFileName = 'key.txt'

with open(keyFileName, 'r') as f:
    key_file_content = f.readline()

with open(fileName, 'r') as f:
    marks_file_content = f.readlines()

answerKey = [i for i in key_file_content.split(
    ' ') if i.isalnum() and len(i) == 1]

students = {}
for student in marks_file_content:
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
