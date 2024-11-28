# Write a function to flatten a list of lists.
def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

print(flatten_list([[1, 2], [3, 4], [5]])) 