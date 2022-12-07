#create a list of integers and find the greatest and lowest

list = []

for i in range(5):
    i = input("Enter a num: ")
    list.append(i)

print("Max = ", max(list))
print("Min = ", min(list))
