#playing with lists

name1 = ["L", "Light", "Kira", "Misa", "N"]

print(name1.index("Misa"))

name2 = ["Ryuk", "Yagami", "Riyuzaki"]

name1.extend(name2)

print(name1)

name3 = input("Enter a name: ")

name1.append(name3)

name1.sort()

name3  = name1[::-1]

print(name1)
print(name3)
