from shift_cipher import encrypt, decrypt

text = input("Enter text: ")
key = int(input("Enter key: "))

encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
