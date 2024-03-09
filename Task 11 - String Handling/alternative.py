""" (alternative.py) This script contains two functions designed to manipulate the case of characters and words 
in a string for stylistic purposes. The 'alternate_character_case' function changes the case of each character alternately 
throughout the string, starting with lowercase. The 'alternate_word_case' function alternates the case of entire words in a string, 
beginning with lowercase for the first word. These functions are useful for creating 
text with a distinctive stylistic pattern. """

# Function to alternate the case of each character in a string
def alternate_character_case(s):
    result = ""  # Initialise an empty string to store the result

    # Iterate over each character in the string, using its index
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].lower()  # For even indices, add the character in lowercase to the result
        else:
            result += s[i].upper()  # For odd indices, add the character in uppercase to the result

    return result  # Return the final string with alternated character case

# Testing the function with a sample string
print(alternate_character_case("Hello World"))  # Output: "hElLo wOrLd"

# Function to alternate the case of each word in a string
def alternate_word_case(s):
    words = s.split()  # Split the string into a list of words

    # Iterate over the list of words, using the index of each word
    for i in range(len(words)):
        # Set words at even indices to lowercase and at odd indices to uppercase
        words[i] = words[i].lower() if i % 2 == 0 else words[i].upper()

    return " ".join(words)  # Join the list of words back into a string and return

# Testing the function with a sample string
print(alternate_word_case("I am learning to code")) # Output: "i AM learning TO code"
