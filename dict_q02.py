# Merge two dictionaries into one. If there are overlapping keys, the second dictionary should overwrite the first.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)
