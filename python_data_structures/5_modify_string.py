#!/usr/bin/python3#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""
def remove_char(some_string):
    char_to_remove = 'a'

    lines = some_string.split('\n')
    for i in range(len(lines)):
        lines[i] = ''.join(char for char in lines[i] if char.lower() != char_to_remove.lower())

    modified_string = '\n'.join(lines)

    return modified_string

result = remove_char(string)
print(result)
