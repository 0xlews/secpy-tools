import argparse

def caesar_cipher(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                shifted = shifted.upper()
            decrypted_text += shifted
        else:
            decrypted_text += char
    return decrypted_text

def main():
    parser = argparse.ArgumentParser(description='Caesar Cipher Decryption')
    parser.add_argument('-t', '--text', type=str, required=True, help='Encrypted text to decrypt')

    args = parser.parse_args()
    encrypted_text = args.text

    for shift in range(26):
        decrypted_text = caesar_cipher(encrypted_text, shift)
        print(f"Shift {shift}: {decrypted_text}")

if __name__ == "__main__":
    main()
