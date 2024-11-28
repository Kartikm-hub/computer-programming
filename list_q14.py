# Write a function that returns the union of two lists (all unique elements).
def list_union(lst1, lst2):
    return list(set(lst1) | set(lst2))

print(list_union([1, 2, 3], [3, 4, 5]))