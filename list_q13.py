# Write a function that returns the intersection of two lists (common elements).
def list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(list_intersection([1, 2, 3], [3, 4, 5]))