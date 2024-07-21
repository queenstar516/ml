def findNum(list, num):
    for item in list:
        if item == num:
            return list.index(num)
    return -1

numbers = [1, 2, 3, 4, 5, 6]
# print(findNum(numbers, 5))

string = "Hello, world"
def countLetter(str, letter):
    count = 0
    i = 0
    while i < len(str):
        if str[i] == letter:
            count += 1
        i += 1
    return count
    
print(countLetter(string, "l"))

def findLetterIndices(str, letter):
    indices = []
    i = 0
    while i < len(str):
        if str[i] == letter:
            indices.append(i)
        i += 1
    return indices

print(findLetterIndices(string, "l"))

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def createNewList(list):
    newList = []
    i = 0
    while i < len(list):
        newList.append(list[i])
        i += 1
    return newList
print(createNewList(integers)) 



#Lambda Functions
x = lambda a: a + 10
print(x(2)) 

add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
mod = lambda a, b: a % b
div = lambda a, b: a / b

print(add(5, 3))
print(sub(89, 34))


def newFunc(y):
    return lambda a: a * y

n = newFunc(6)
print(n(2))



#Try.....Except
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(ZeroDivisionError)
        return "An exception occurs"
    finally:
        return "No exception"

print(div(2, 0))