
"""
░█▀▄░█▀▀░█░█░█▀▀░█▀▄░█░█░█▀█░▀█▀
░█▀▄░█░░░░▀█░█░░░█▀▄░░█░░█▀▀░░█░
░▀░▀░▀▀▀░░░▀░▀▀▀░▀░▀░░▀░░▀░░░░▀░
"""

from Crypto.Cipher import ARC4
import argparse
import sys

# Function to encrypt using RC4
def rc4_encrypt(key, plaintext):
    cipher = ARC4.new(key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

# Function to decrypt using RC4
def rc4_decrypt(key, ciphertext):
    cipher = ARC4.new(key)
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text

# Main function
def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a message using RC4.")
    
    # Define cli arguments
    parser.add_argument("-o", "--operation", choices=["encrypt", "decrypt"], help="Specify 'encrypt' or 'decrypt'.")
    parser.add_argument("-k", "--key", help="Encryption/decryption key (in bytes).")
    parser.add_argument("-m", "--message", help="Message to be encrypted or decrypted (in bytes).")
    
    args = parser.parse_args()

    # Check if no arguments were provided
    if len(sys.argv) == 1:
        print(__doc__)  # Print ASCII art
        parser.print_help()  # Print help message
        sys.exit(1)  # Exit the script

    # Convert the key to bytes
    key = args.key.encode()

    # Perform encryption or decryption based on the specified operation
    if args.operation == "encrypt":
        result = rc4_encrypt(key, args.message.encode())
        print("Ciphertext:", result.hex())
    else:
        # Convert the hex-encoded message back to bytes and then decrypt
        result = rc4_decrypt(key, bytes.fromhex(args.message))
        print("Decrypted text:", result.decode())

if __name__ == "__main__":
    main()
