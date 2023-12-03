#!/usr/bin/python3

# copy of the string, removing the character at the position n
def remove_char_at(str, n):
    output = ""  # an empty string
    length = len(str)  # length of the string
    for a in range(length):
        if a == n:
            continue
        output += str[a]  # concatenate the string to the output
    return output
