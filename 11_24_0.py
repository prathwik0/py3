#lists in python

l1 = [1,2,3.3]
l2 = ["L", "L", "Light", "Misa"]

l3 = l1 + l2

print(l3)

print(l3.count("L"))

l3.append("Kira")

l3.extend(l2)

l3.insert(0, "N")

print(l3)

print(l3.pop())

print(l3.index("N"))

l3.reverse()

print(l3)

l3.remove("L")
l3.remove("L")

print(l3)

l4 = [5, 7, 3.1, 99, 0.0012, 31]

print("Max = ", max(l4), "Min = ", min(l4))

l4.sort()

print(l4)
