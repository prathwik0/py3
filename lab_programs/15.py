# Design a class named Rectangle to represent a rectangle.
# class contains:Two data fields named width and height.
# A constructor that creates a rectangle with the specified width and height.
# A method named getArea() that returns the area of this rectangle.

# Write a program that creates ‘n’ number of Rectangle objects.
# Read values of widthand height from the key board for each Rectangle instance.
# Display the width and height of the rectangle having maximum and min area.

class rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width*height

    def getArea(self):
        return self.area

    def print(self):
        print("height", self.height, "width", self.width, "area", self.area)


def maxArea(list):
    max = list[0]

    for rect in list:
        if rect.getArea() > max.area: #ATQ (acc to the ques getArea() func is to be called for the area of the reactangle
            max = rect
    return max


def minArea(list):
    min = list[0]

    for rect in list:
        if rect.getArea() < min.area: #ATQ (acc to the ques getArea() func is to be called for the area of the reactangle
            min = rect
    return min


def main():
    list = []

    n = int(input("Enter n:"))
    for i in range(n):
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        list.append(rect(width, height))
        list[i].print()

    max = maxArea(list)
    min = minArea(list)

    print("Max area rect:")
    max.print()

    print("Min area rect:")
    min.print()


main()
