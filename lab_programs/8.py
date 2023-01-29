a1 = input("Enter string1: ")
a2 = input("Enter string2: ")

a = ""

for i in a1:
    if (i.isupper()):
        a = a + i

for i in a2:
    if (i.isupper()):
        a = a + i

print("The merged string is", a)
