# Write a function to multiply all elements in a list.
def multiply_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result

print(multiply_elements([1, 2, 3, 4]))         