# Write a Bubble sort function which will sort the given numbers.
# The function should return the sorted list.

def bubbleSort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def main():
    list = [5, 2, 1, 8, 0, 100, 20, -5]
    sortedList = bubbleSort(list)

    print("unsorted list:", list)
    print("sorted list:", sortedList)


main()
