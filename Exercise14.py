# Exercise 14
"""
Caesar Cipher

A Caesar cipher shifts each letter in a message by a fixed number of positions in the alphabet. For example with shift 3: A→D, B→E, Z→C.

Write a function `encrypt(message, shift)` that encodes the message.
Write a function `decrypt(message, shift)` that decodes it.

Rules:
- Only shift letters, leave spaces and punctuation unchanged
- Wrap around (after Z comes A again)
- Preserve uppercase and lowercase

Test:
- Encrypt `"Hello World"` with shift `3` → should give `"Khoor Zruog"`
- Decrypt `"Khoor Zruog"` with shift `3` → should give `"Hello World"`
- Encrypt and then decrypt `"Python is fun!"` with shift `13` — should get back the original

Hint: look up `ord()` and `chr()` on W3Schools.
"""

def encrypt(message, shift):
    encrypted_message = ""

    for char in message:
        if char.isupper():
            encrypted_message += chr(
                (ord(char) - ord('A') + shift) % 26 + ord('A')
            )
        elif char.islower():
            encrypted_message += chr(
                (ord(char) - ord('a') + shift) % 26 + ord('a')
            )
        else:
            encrypted_message += char
        
    return encrypted_message
    
def decrypt(message, shift):
    decrypted_message = ""

    for char in message:
        if char.isupper():
            decrypted_message += chr(
                (ord(char) - ord('A') - shift) % 26 + ord('A')
            )
        elif char.islower():
            decrypted_message += chr(
                (ord(char) - ord('a') - shift) % 26 + ord('a')
            )
        else:
            decrypted_message += char

    return decrypted_message

# test 1
encrypted = encrypt("Hello World", 3)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, 3)
print("Decrypted:", decrypted)
print()

# test 2
message = "Python is fun!"
encrypted = encrypt(message, 13)
decrypted = decrypt(encrypted, 13)

print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
        