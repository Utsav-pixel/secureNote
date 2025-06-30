def caesar_encrypt(text: str, shift: int = 3) -> str:
    result = ""
    for char in text:
        if char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def caesar_decrypt(cipher: str, shift: int = 3) -> str:
    result = ""
    for char in cipher:
        if char.islower():
            result += chr((ord(char) - 97 - shift) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += char
    return result