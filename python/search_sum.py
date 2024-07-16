def printList(list):
    for element in list:
        print(element)

names = ["James", "Jane", "Paula", "Paul"]

printList(names)

def findSum(list, target):
    i = 0
    while i < len(list):
        j = i + 1
        while j < len(list):
            if list[i] + list[j] == target:
                return [i, j]
            j += 1
        i += 1
    return -1

numbers = [1, 3, 5, 7, 9, 10, 11, 13, 15, 17, 19, 20]
print(findSum(numbers, 19))


def factorialWithLoop(x):
    sum = 1
    i = 1
    while i <= x:
        sum *= i
        i += 1
    return sum

