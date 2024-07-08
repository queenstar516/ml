def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        elif target > potentialMatch:
            left = middle + 1
    return -1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(binarySearch(numbers, 4))


#palindromes
def determinePalindrome(string):
    start = 0
    end = len(string) - 1
    while start <= end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True
    

print(determinePalindrome("121"))