#Task 1
def reverse_string(string):
    reversedString = ""
    i = len(string) - 1
    while i >= 0:
        reversedString += string[i]
        i -= 1
    print(reversedString)

word = "supercalifragilisticexplialidocious"
reverse_string(word)

#Task 2
def sumNumbers(num):
    total = 0
    i = 1
    while i <= num:
       total += i
       i += 1  
    print(total)
sumNumbers(50)


#Task 3
def fizzBuzz():
    i = 1
    while i <= 100:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1

fizzBuzz()