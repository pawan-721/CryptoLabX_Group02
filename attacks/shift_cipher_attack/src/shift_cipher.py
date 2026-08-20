def encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            start = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - start + key) % 26 + start)
        else:
            result += ch

    return result


def decrypt(text, key):
    return encrypt(text, -key)


if __name__ == "__main__":
    text = input("Enter text: ")
    key = int(input("Enter key: "))

    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, key)

    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
