#find factorial of a number using while loop

n = int(input("Enter n : "))

print("The factorial of n is :")

fact = 1

while (n != 0):
    fact = fact * n
    n = n - 1

print(fact)

i = 1
while (i <= n):
    fact = fact * i
    i = i + 1
    

print("\n",fact)
