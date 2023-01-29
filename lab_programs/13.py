# Suppose that a text file contains marks for 6 courses for a
# student in a line. Each coursemarks is separated by space as
# delimiter. File contains marks for ‘n’ number of students in
# separate lines. Write a program that readsthe marks from the
# file for each student and displays the total and average.
# Your program should prompt the user to enter a filename.

filename = input("Enter the filename: ")

with open(filename, 'r') as f:
    lines = f.readlines()

i = 1
for line in lines:
    marks = line.split(' ')

    marks = [int(i) for i in marks]

    # marks2 = []

    # for i in marks:
    #     marks2.append(int(i))

    total = sum(marks)

    avg = total/len(marks)

    print("Student", i, " Total: ", total, "Average: ", avg)
    i += 1
