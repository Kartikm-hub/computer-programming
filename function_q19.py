# Write a function that takes two lists and returns a list with their common elements.
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(common_elements([1, 2, 3], [2, 3, 4]))