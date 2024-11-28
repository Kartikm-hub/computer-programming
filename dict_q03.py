# Check if a given key exists in a dictionary. If it exists, print its value. Otherwise, print a message saying the key does not exist.
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
key = 'age'
if key in my_dict:
    print(f"The value of '{key}' is {my_dict[key]}")
else:
    print(f"'{key}' does not exist in the dictionary")
