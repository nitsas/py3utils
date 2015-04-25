"""
Translate a string to ROT13 and back. 

Usage: Just call the translate function with your string.

Non-ASCII-letter characters will not be affected.
"""


from string import ascii_letters, ascii_lowercase, ascii_uppercase


ascii_lowercase_rot13 = ascii_lowercase[13:] + ascii_lowercase[:13]
ascii_uppercase_rot13 = ascii_uppercase[13:] + ascii_uppercase[:13]
ascii_letters_rot13 = ascii_lowercase_rot13 + ascii_uppercase_rot13


rot13_translation_table = str.maketrans(ascii_letters, ascii_letters_rot13)


# users will call this to do the translation
def translate(text):
    """
    Translate a string to ROT13.
    
    text -- a Python string
    
    Non-ASCII-letter characters will not be affected.
    """
    return text.translate(rot13_translation_table)


# define two aliases for the function:
rot13 = convert = translate 
