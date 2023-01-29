A = input("Enter string: ") 
a = A.lower()

count = 0
dict = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0} 

for i in a:
    if i in ["a","e","i","o","u"]:
        dict[i] += 1
        count += 1

print(dict)
print("No. of vowels = ", count)