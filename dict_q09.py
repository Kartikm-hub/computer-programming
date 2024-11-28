# Create a dictionary with words as keys and their frequencies as values. Write a function to return the word with the highest frequency.
def get_most_frequent_word(word_dict):
    return max(word_dict, key=word_dict.get)

word_dict = {'apple': 3, 'banana': 1, 'cherry': 5}
print(get_most_frequent_word(word_dict))