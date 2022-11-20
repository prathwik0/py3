#while loop - print sum of n natural numbers

n = int(input("Enter n :"))

print("The sum of first n natural numbers is :")

sum = 0

while (n != 0):
    sum = sum + n
    n = n - 1

print(sum)
