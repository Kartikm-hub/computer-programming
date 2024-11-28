# Write a function that returns the difference between the largest and smallest number in a list.
def difference_max_min(lst):
    return max(lst) - min(lst)

print(difference_max_min([10, 20, 5, 8]))