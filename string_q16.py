# Find the longest word in a string.
my_string = "I am learning Python programming"
words = my_string.split()
longest_word = max(words, key=len)
print(longest_word)