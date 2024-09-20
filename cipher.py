# Importing libraries.
import string

# Print alphabetic characters.
alphabet = list(string.ascii_uppercase)
print(alphabet)     # Testing.

shift = 1
message = 'ABCDEFG'


# Function to encrypt a message.
def encrypt(message, shift):
    encrypted_message = ""
    for character in message:
        # For each character in the message, check if it is in the alphabet.
        if character in alphabet:
            index = alphabet.index(character)           # Index.
            new_position = (index + shift) % 26         # Ensure wrapping around
            encrypted_message += alphabet[new_position]
        else:
            encrypted_message += character              # Keep non-alphabet characters unchanged
    return encrypted_message                            # Return to for loop.


# Function to decrypt a message.
def decrypt():
    pass


print(encrypt(message, shift))
