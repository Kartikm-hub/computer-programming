# Write a function to find the sum of all positive numbers in a list.
def sum_positive(lst):
    return sum(x for x in lst if x > 0)

print(sum_positive([1, -2, 3, 4]))