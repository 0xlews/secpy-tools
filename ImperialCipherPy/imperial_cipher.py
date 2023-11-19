
"""
╦╔╦╗╔═╗╔═╗╦═╗╦╔═╗╦    ╔═╗╦╔═╗╦ ╦╔═╗╦═╗  ┌─┐┬ ┬
║║║║╠═╝║╣ ╠╦╝║╠═╣║    ║  ║╠═╝╠═╣║╣ ╠╦╝  ├─┘└┬┘
╩╩ ╩╩  ╚═╝╩╚═╩╩ ╩╩═╝  ╚═╝╩╩  ╩ ╩╚═╝╩╚═  ┴   ┴ 
"""

import argparse
import sys

# Function to perform Caesar Cipher
def caesar_cipher(text, shift, encrypt=True):
    shifted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shift_factor = shift if encrypt else -shift # Calc shift factor. If encrypting, use shift as is; if decrypting, use negative of shift
            shifted_char = chr(((ord(char) - ord('a') + shift_factor) % 26) + ord('a')) # Perform shift operation and get the ASCII value
            if is_upper:
                shifted_char = shifted_char.upper() # Convert back to uppercase if original was upper
            shifted_text += shifted_char
        else:
            shifted_text += char # If char is not an alphabet letter, add to the result string as is
    return shifted_text

# Argument parsing
parser = argparse.ArgumentParser(description="ImperialCipherPy - A tool for Caesar Cipher encryption and decryption")
parser.add_argument("-e", "--encrypt", help="Encrypt the message", action="store_true")
parser.add_argument("-d", "--decrypt", help="Decrypt the message", action="store_true")
parser.add_argument("-t", "--text", help="The text to encrypt or decrypt", type=str, required=True)
parser.add_argument("-s", "--shift", help="Shift value for the cipher", type=int, required=True)

# Check if no arguments were provided
if len(sys.argv) == 1:
    print(__doc__)  # Print ASCII art
    parser.print_help()  # Print help message
    sys.exit(1)  # Exit the script

args = parser.parse_args()

if args.encrypt:
    print("Encrypted Message:", caesar_cipher(args.text, args.shift))
elif args.decrypt:
    print("Decrypted Message:", caesar_cipher(args.text, args.shift, False))
else:
    parser.print_help()
