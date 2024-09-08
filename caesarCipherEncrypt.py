def caesarCipherEncrypt(string, key):
    newString = []
    key = key % 26  # Ensure the key is within 0-25

    for letter in string:
        if letter.isalpha():  # Check if the character is a letter
            newString.append(getNewLetter(letter, key))
        else:
            newString.append(letter)

    return ''.join(newString)


def getNewLetter(letter, key):
    if letter.islower():  # Check for lowercase letters
        newLetterCode = ord(letter) + key
        if newLetterCode > ord('z'):  # Wrap around if necessary
            newLetterCode -= 26
    elif letter.isupper():  # Check for uppercase letters
        newLetterCode = ord(letter) + key
        if newLetterCode > ord('Z'):  # Wrap around if necessary
            newLetterCode -= 26
    return chr(newLetterCode)


# Example usage

string = "Hello, World!"
key = 3
encrypted_string = caesarCipherEncrypt(string, key)
print("Encrypted string:", encrypted_string)
