import string 

a = input("Enter string: ")

for i in a:
    if i in string.punctuation:
        a = a.replace(i, '')
        
print(a)
