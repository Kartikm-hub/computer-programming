# Check if a string is a palindrome (reads the same forward and backward).
def is_palindrome(s):
    return s == s[::-1]

my_string = "madam"
print(is_palindrome(my_string))