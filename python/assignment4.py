#Task 1
word = "supercalifragilisticexplialidocious"
print(word[::-1])

#Task 2
def numbers(num):
    i = 0
    while i <= num:
        print(i)
        i += 1
numbers(50)


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