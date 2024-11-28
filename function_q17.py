# Write a function to find the least common multiple (LCM) of two numbers.
def lcm(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return abs(a * b) // gcd(a, b)

print(lcm(4, 5))