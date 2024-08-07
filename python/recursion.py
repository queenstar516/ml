def tri_recursion(k):
    if k > 0:
      result = k + tri_recursion(k - 1)
      print(result)
    else:
      result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#Lambda Function
x = lambda a, b, c: print(a, b, c)

print(x(5, 4, 3))

#Palindrome using recursion
def isPalindrome(word):
   word = word.lower()

   if len(word) <= 1:
      return True
   
   if word[0] == word[-1]:
      return isPalindrome(word[1 : -1])
   
   return False

print(isPalindrome("racecar"))
print(isPalindrome("hello"))
print(isPalindrome("madam"))