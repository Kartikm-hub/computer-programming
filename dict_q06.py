# Write a Python function that takes a dictionary as an argument and returns a list of all keys with values greater than a given threshold.
def filter_keys_by_value(d, threshold):
    return [key for key, value in d.items() if value > threshold]

my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
result = filter_keys_by_value(my_dict, 10)
print(result)