# Write a function that returns a string in alternating uppercase and lowercase letters.
def alternate_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

print(alternate_case("hello"))