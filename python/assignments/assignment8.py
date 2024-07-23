#assignment 1
even_num = []

for num in range(1, 51):
    try:
        if num % 2 == 0:
            even_num.append(num)
    except Exception as e:
        print(f"An error occurred: {e}")

print(even_num)


#assignment 3
def get_valid_score(prompt, max_score):
    while True:
        try:
            score = int(input(prompt))
            if 0 <= score <= max_score:
                return score
            else:
                print(f"LOL, you know that's not possible. Input a valid score between 0 and {max_score}.")
        except ValueError:
            print("Please enter a valid integer.")

assignment_score = get_valid_score("Assignment(20): ", 20)
test_score = get_valid_score("Test(20): ", 20)
exam_score = get_valid_score("Exam(60): ", 60)

# Calculating total score
total = assignment_score + test_score + exam_score

# Determine grade based on total score
if total >= 70:
    print(f"Your total score is {total}. Congratulations, you have an A.")
elif total >= 60:
    print(f"Your total score is {total}. Good job, you have a B.")
elif total >= 50:
    print(f"Your total score is {total}. Mid, you have a C.")
elif total >= 40:
    print(f"Your total score is {total}. Try better next time, you have a D.")
else:
    print(f"Your total score is {total}. See you next year, you have an F.")




#assignment 4

#task 1
def reverse_string(string):
    try:
        reversedString = ""
        i = len(string) - 1
        while i >= 0:
            reversedString += string[i]
            i -= 1
        print(reversedString)
    except Exception as e:
        print(f"An error occurred: {e}")

word = "supercalifragilisticexplialidocious"
reverse_string(word)

#task 2
def sumNumbers(num):
    try:
        total = 0
        i = 1
        while i <= num:
            total += i
            i += 1  
        print(total)
    except Exception as e:
        print(f"An error occurred: {e}")

try:
    num = int(input("Enter a number: "))
    sumNumbers(num)
except ValueError:
    print("Please enter a valid integer.")

#task 3
def fizzBuzz():
    try:
        i = 1
        while i <= 100:
            try:
                if i % 3 == 0 and i % 5 == 0:
                    print("FizzBuzz")
                elif i % 3 == 0:
                    print("Fizz")
                elif i % 5 == 0:
                    print("Buzz")
                else:
                    print(i)
                i += 1
            except Exception as e:
                print(f"An error occurred at {i}: {e}")
                break
    except Exception as e:
        print(f"An error occurred: {e}")

fizzBuzz()



#assignment 5
letters = {
    "e": "3",
    "A": "4",
    "b": "6",
    "B": "8",
    "o": "0",
    "I": "1",
    "S": "5",
    "f": "7",
    "p": "9",
    "Z": "2"
}

def replaceLetters(word, letters_dict):
    try:
        replacedWord = ""
        for char in word:
            if char in letters_dict:
                replacedWord += letters_dict[char]
            else:
                replacedWord += char
        return replacedWord
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

orgWord = "Hello, I am a Bot"
print(replaceLetters(orgWord, letters))



#assignment 6
def calculateParkingFee(hours):
    try:
        # Ensure hours is a valid non-negative integer
        if hours < 0:
            raise ValueError("Number of hours cannot be negative.")
        
        fee = 0
        if hours <= 5:
            fee = hours * 1
        elif hours > 5 and hours < 24:
            fee = 5 + ((hours - 5) * 0.5)
        elif hours == 24:
            fee = 15
        elif hours % 24 == 0:
            fee = 15 * (hours / 24)
        elif hours > 24:
            fee = 15 + ((hours - 24) * 0.5)
        
        return f"Your fee is ${fee:.2f}"
    except ValueError as ve:
        return f"Invalid input: {ve}"
    except Exception as e:
        return f"An error occurred: {e}"

try:
    hours = int(input("Input number of hours: "))
    print(calculateParkingFee(hours))
except ValueError:
    print("Please enter a valid integer for the number of hours.")



#assignment 7

#String reversal with recursion
def reverse_string_recursive(s):
    try:
        if len(s) <= 1:
            return s
        return s[-1] + reverse_string_recursive(s[:-1])
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

s = "hello"
print(reverse_string_recursive(s))

#Checking if a word is a palindrome with recursion
def is_palindrome_recursively(s):
    try:
        if len(s) <= 1:
            return True
        if s[0] == s[-1]:
            return is_palindrome_recursively(s[1:-1])
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

s = "racecar"
print(is_palindrome_recursively(s))


#Binary search with recursion
def binary_search_recursive(array, target, left, right):
    try:
        if left > right:
            return -1
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif target < array[middle]:
            return binary_search_recursive(array, target, left, middle - 1)
        else:
            return binary_search_recursive(array, target, middle + 1, right)
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search_recursive(array, target, 0, len(array) - 1)
print(result)

