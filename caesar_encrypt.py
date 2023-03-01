def encrypt(text, shift): 
    """Encrypts plaintext using the Caesar cipher"""
    result = "" 

    # traverse text 
    for char in text:
        # If character is uppercase, shift its Unicode code point by 'shift'
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # If character is lowercase, shift its Unicode code point by 'shift'
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char # If character is not an alphabet, do not shift it.

    return result
