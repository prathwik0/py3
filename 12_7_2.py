a = input("Enter string: ")

count = 0

for i in a:
    if i in ['a', 'e', 'i', 'e', 'o', 'A', 'E', 'I', 'O', 'U']:
        count = count + 1

print("The total num of vovels is:", count)
