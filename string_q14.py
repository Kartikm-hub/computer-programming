# Check if a string contains any uppercase characters.
my_string = "Hello World"
contains_upper = any(char.isupper() for char in my_string)
print(contains_upper)