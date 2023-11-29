# function defining  to remove vowels by taking parameter as input string
#define vowels 
def remove_vowels(input_string):
    result = ""
    vowels = "aeiouAEIOU"
# using for loop  
# Iterate through each character in the input string

    for i in input_string:
 # Check if the current character is not a vowel

        if i not in vowels:
            result += i
#final result
    return result

input_string = "Sameena!"
output_string = remove_vowels(input_string)

print("Input String:", input_string)
print("Output String:", output_string)
