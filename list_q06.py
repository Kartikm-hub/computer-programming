# Write a function that returns a list of even numbers from a given list.
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

print(even_numbers([1, 2, 3, 4, 5, 6]))