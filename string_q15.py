# Remove all punctuation from a string.
import string
my_string = "Hello, world! How's it going?"
clean_string = my_string.translate(str.maketrans('', '', string.punctuation))
print(clean_string)