# Write a function that rotates a list n positions to the right.
def rotate_list(lst, n):
    return lst[-n:] + lst[:-n]

print(rotate_list([1, 2, 3, 4, 5], 2))