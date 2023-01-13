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
        if rect.area > max.area:
            max = rect
    return max

def minArea(list):
    min = list[0]
    
    for rect in list:
        if rect.area < min.area:
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
