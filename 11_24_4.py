#program to divide a list into 2 lists
#one with odd numbers and the other with even numbers


list = []
listo = []
liste = []


n = int(input("Enter n: "))

for i in range(n):
    j = int(input())
    list.append(j)

    
for i in list:
    if (i % 2) == 0:
        liste.append(i)
    else:
        listo.append(i)

print("List     :", list)
print("Odd list :", listo)
print("Even list:", liste)
