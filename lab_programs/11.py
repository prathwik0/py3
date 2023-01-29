# Write a Bubble sort function which will sort the given numbers.
# The function should return the sorted list.

def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1 - i):
            if (list[j] > list[j+1]):
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def main():
    list = [1, 4, 5, 11, 98, 3, 0, 7]
    print(list)
    bubbleSort(list)
    print(list)


main()
