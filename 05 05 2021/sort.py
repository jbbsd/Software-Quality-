import time
import os.path as path


def parseLine(line):
    items = line.split()
    numbers = []
    for item in items:
        if item[0] == "-":
            if item[1:].isdigit():
                numbers.append(int(item))

        if item.isdigit():
            numbers.append(int(item))
        else:
            print("found a non-digit character in the file")

    return numbers


def readFile(filename):
    if filename.lower().endswith('.txt'):
        print("Reading the file...")
        if path.isfile(filename):
            file = open(filename, "r")
            numbers = []
            for line in file:
                items = parseLine(line)
                for item in items:
                    numbers.append(item)
            file.close()
            merge_sort(numbers, 0, len(numbers) - 1)
            print("list of number sorted: ")
            time.sleep(0.3)
            for nb in numbers:
                time.sleep(0.3)
                print("- " + str(nb))
        else:
            print("file doesnt exist")
    else:
        print("not correct format")


def shellSort(array):
    n = len(array)
    gap = n // 2
    print("The list of number is under treatment... ")
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    time.sleep(1)
    print("list of number sorted: ")
    time.sleep(0.5)
    for nb in array:
        time.sleep(0.3)
        print("- " + str(nb))


def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)


def merge(array, left_index, right_index, middle):
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle + 1:right_index + 1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


if __name__ == '__main__':
    readFile("numbers.txt")
