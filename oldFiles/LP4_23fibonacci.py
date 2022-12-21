#fibonacci series

print("Fibonacci Series")
n = int(input("Enter the number of terms : "))

a = 0
b = 1

while(n != 0):
    print(a)
    temp = a
    a = b
    b = temp + a
    n = n - 1
