# Write a function that takes a list and returns the second smallest number.
def second_smallest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[1] if len(unique_lst) > 1 else None

print(second_smallest([4, 2, 5, 1, 3]))