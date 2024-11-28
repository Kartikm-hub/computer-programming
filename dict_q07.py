# Create a dictionary where keys are letters ('a' to 'f') and values are the corresponding numbers (1 to 6). Then, sort the dictionary by keys and print the sorted dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)