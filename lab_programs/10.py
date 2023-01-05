n = int(input("Enter a number: "))
n2 = n

nReverse = 0

while (n2 != 0):
    nReverse = (nReverse * 10) + n2 % 10
    n2 = int(n2/10)

print("Reverse:", nReverse)

if (nReverse == n):
    print("It is a palindrome number!")
else:
    print("Not palindrome")
