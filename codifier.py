from alphabets import small_alphabet

def caesarCipher(text: str, offset: int = 3, alphabet: str = small_alphabet) -> str:
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
        pos = alphabet.find(char)
        if pos != -1:
            cipher += alphabet[(pos + offset) % len(alphabet)]
        else:
            cipher += char
    return cipher

def keywordCipher(text: str, key: str, baseAlphabet: str = small_alphabet) -> str:
    """
    Encrypts a string using the substitution cipher.

    :params:
        text: str
            The text to encrypt.
        key: str
            The key to use for the cipher.
    
    :returns:
        The encrypted text.
    """

    # normalize the key
    for char in set(key):
        if char not in baseAlphabet:
            if char.isalpha():
                if char.islower() and char.upper() in baseAlphabet:
                    key = key.replace(char, char.upper())
                    continue
                elif char.lower() in baseAlphabet:
                    key = key.replace(char, char.lower())
                    continue
                
            key = key.replace(char, "")

    
    # remove duplicate characters from the key in the same order
    key = "".join(sorted(set(key), key=key.index))

    # creating the new alphabet based on the key
    newAlphabet = key
    newAlphabet += ''.join([baseAlphabet[(i + baseAlphabet.find(key[-1]) + 1) % len(baseAlphabet)]
        for i in range(len(baseAlphabet) -1)
        if baseAlphabet[(i + baseAlphabet.find(key[-1]) + 1) % len(baseAlphabet)] not in key])

    # reemplacing the alphabet
    
    cipher = ''
    for char in text:
        pos = baseAlphabet.find(char)
        if pos != -1:
            cipher += newAlphabet[pos]
        else:
            cipher += char
    
    return cipher