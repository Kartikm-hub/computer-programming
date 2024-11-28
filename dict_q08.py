# Write a Python program to combine two dictionaries into one and sum the values of overlapping keys.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

result = dict1.copy()
for key, value in dict2.items():
    result[key] = result.get(key, 0) + value

print(result)