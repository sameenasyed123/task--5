#print number of words in a string

def count_words(input_string):
    # Split the input string into a list of words
    words = input_string.split()

    # Return the number of words in the list
    return len(words)

input_str = "Hello world! This is a sample sentence."
result = count_words(input_str)
print(f"The number of words is: {result}")
