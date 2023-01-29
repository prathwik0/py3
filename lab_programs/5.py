a = input("Enter string: ")

pos = 0
count = 0

for i in a:
    if (i.isupper()):
        count = count + 1
        print(i, "at position", pos)
    pos = pos + 1

print("The total num of Capital letters is:", count)
