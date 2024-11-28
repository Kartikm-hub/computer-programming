# Write a function that removes all occurrences of a specific element from a list.
def remove_element(lst, element):
    return [x for x in lst if x != element]

print(remove_element([1, 2, 3, 4, 2], 2))