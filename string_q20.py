# Check if a string is an anagram of another string.
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

string1 = "listen"
string2 = "silent"
print(is_anagram(string1, string2))