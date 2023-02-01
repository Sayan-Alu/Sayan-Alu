

#    Python program that takes the string and the replacement character
#  as input from the user and replaces spaces in the string with the given character


def replace_space(string, char):

    return string.replace(" ", char)

input_str = input("Enter a string: ")

replacement_char = input("Enter a character to replace spaces: ")

output_str = replace_space(input_str, replacement_char)

print("Output string:", output_str)