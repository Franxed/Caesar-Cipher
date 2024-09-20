# Importing libraries.
import string

# Print alphabetic characters.
alphabet = list(string.ascii_letters)


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
    return encrypted_message


# Function to decrypt a message. [Same principal as encrypt().]
def decrypt(message, shift):
    decrypted_message = ""
    for character in message:
        if character in alphabet:
            index = alphabet.index(character)
            original_position = (index - shift) % 26
            decrypted_message += alphabet[original_position]
        else:
            decrypted_message += character
    return decrypted_message


# Main function to handle the user.
def main():
    while True:
        try:
            query = int(input("Would you like to:\n 1.) Encrypt\n2.) Decrypt \n: "))
            if query == 1:
                message = input("Enter your message: ")
                shift = int(input("Enter the shift value: "))
                encrypted_message = encrypt(message, shift)
                print(f"\nYour encoded message: {encrypted_message}")

            elif query == 2:
                message = input("Enter your encrypted message: ")
                shift = int(input("Enter the shift value: "))
                decrypted_message = decrypt(message, shift)
                print(f"Your decoded message: {decrypted_message}")
            break
        except ValueError as va:
            print(f"Error - {va}.\n")


# Run main loop.
if __name__ == '__main__':
    main()
