# print number of  unique characters ina string
def count_unique_characters(input_string):
    # Use a set to store unique characters
    unique_chars = set()

    # Iterate through each character in the input string
    for char in input_string:
        # Add the character to the set
        unique_chars.add(char)

    # Return the number of unique characters
    return len(unique_chars)

# Example usage:
input_str = "hello, world!"
unique_char_count = count_unique_characters(input_str)
 #Print the original input string and the number of unique characters
print("Input String:", input_str)
print("Number of Unique Characters:", unique_char_count)
