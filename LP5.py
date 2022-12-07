#find sum of even and odd numbers
n = int(input("Enter n :"))
esum = 0
osum = 0
i = 0
print("Enter the numbers")
while (i < n):
    a = int(input())
    if(a%2 == 0):
       esum = esum + a
    else:
        osum = osum + a
    i = i + 1
print("Even sum =", esum)
print("Odd sum =", osum)
