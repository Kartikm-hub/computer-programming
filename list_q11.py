# Write a function that checks if a list is sorted.
def is_sorted(lst):
    return lst == sorted(lst)

print(is_sorted([1, 2, 3, 4]))  
print(is_sorted([4, 3, 2, 1]))