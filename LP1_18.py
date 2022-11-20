#read student details with name, roll no. and three marks
#find average and display the grade

student=  ["",""]
mark = [0,0,0]

student[0] = input("Enter the name : ")
student[1] = input("Enter the roll number : ")
mark[0] = int(input("Enter mark 1 : "))
mark[1] = int(input("Enter mark 2 : "))
mark[2] = int(input("Enter mark 3 : "))

avg = (mark[0] + mark[1] + mark[2] ) / 3.0

fail = False

for i in mark :
    if i < 35 :
        print("FAILED")
        fail = True


if fail !=  True:
    print("The average marks is", avg)
    if avg >= 90:
        print("Grade S")
    elif avg >= 80:
        print("Grade A")
    elif avg >= 70:
        print("Grade B")
    elif avg >= 50:
        print("Grade C")
    else:
        print("Pass")




