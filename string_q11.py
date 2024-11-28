# Count the number of vowels in a string.
my_string = "Hello world"
vowels = "aeiou"
count = sum(1 for char in my_string.lower() if char in vowels)
print(count)