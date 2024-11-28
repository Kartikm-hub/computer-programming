# Write a function that accepts a list and returns a new list with only the even numbers.
def filter_even(lst):
    return [num for num in lst if num % 2 == 0]

print(filter_even([1, 2, 3, 4, 5, 6]))