# Write a Python program to generate first ‘n ’Fibonacci numbers.

n = int(input("Enter n: "))

first = 0
second = 1

for i in range(n + 1):
    print(first)
    first, second = second, first + second
