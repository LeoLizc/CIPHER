
def caesarCipher(text: str, offset: int = 3) -> str:
    """
    Encrypts a string using the Caesar cipher.

    :params:
        text: str
            The text to encrypt.
        offset: int
            The offset to use for the cipher.
            By default, this is 3.
    
    :returns:
        The encrypted text.
    """

    cipher = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                char = chr((ord(char) + offset - 65) % 26 + 65)
            else:
                char = chr((ord(char) + offset - 97) % 26 + 97)
        cipher += char
    return cipher


if __name__ == '__main__':
    print(caesarCipher('Hello, World!', 3))