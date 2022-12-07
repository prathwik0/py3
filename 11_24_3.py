#for loop in python
#create a dynamic list and find the sum

list = []
sum = 0


n = int(input("Enter n: "))

for i in range(n):
    j = int(input("Enter num: "))
    list.append(j)
    sum = sum + list[i]
    
print("Sum = ", sum)
    

