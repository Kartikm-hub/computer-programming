# Write a program that takes a dictionary and returns a new dictionary with the keys and values swapped (i.e., keys become values and values become keys).
def swap_dict(d):
    return {v: k for k, v in d.items()}

my_dict = {'a': 1, 'b': 2, 'c': 3}
swapped_dict = swap_dict(my_dict)
print(swapped_dict)