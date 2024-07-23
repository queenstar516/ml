#String reversal with recursion
def reverse_string_recursive(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string_recursive(s[:-1])

s = "hello"
print(reverse_string_recursive(s))


#Checking if a word is a palindrome with recursion
def is_palindrome_recursively(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome_recursively(s[1:-1])
    return False

s = "racecar"
print(is_palindrome_recursively(s))


#Binary search with recursion
def binary_search_recursive(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right ) // 2
    if array[middle] == target:
        return middle
    elif target < array[middle]:
        return binary_search_recursive(array, target, left, middle - 1)
    else:
        return binary_search_recursive(array, target, middle + 1, right)
    
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search_recursive(array, target, 0, len(array) - 1)
print(result)