# Write a function that returns whether a string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam")) 