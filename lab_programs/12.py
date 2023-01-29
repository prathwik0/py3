# Write a function that returns the index of the smallest element
# in a list of integers. If the number of such elements is greater
# than 1,return the smallest index. Use the following header:

# def indexOfSmallestElement(lst):

# Write a test program that prompts the user to enter a list of
# numbers, invokes this function to return the index of the smallest
# element and displays the index.

def indexOfSmallestElement(list):
    index = 0
    for i in range(len(list)):
        if (list[i] < list[index]):
            index = i
    return index


def main():
    n = int(input("Enter n: "))
    list = []
    for i in range(n):
        list.append(int(input()))

    print(list)
    print("Index of smallest element is", indexOfSmallestElement(list) + 1)


main()
