from Crypto.Cipher import ARC4
import argparse

def rc4_encrypt(key, plaintext):
    cipher = ARC4.new(key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def rc4_decrypt(key, ciphertext):
    cipher = ARC4.new(key)
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a message using RC4.")
    parser.add_argument("operation", choices=["encrypt", "decrypt"], help="Specify 'encrypt' or 'decrypt'.")
    parser.add_argument("key", help="Encryption/decryption key (in bytes).")
    parser.add_argument("message", help="Message to be encrypted or decrypted (in bytes).")

    args = parser.parse_args()

    key = args.key.encode()  # Encode the key as bytes
    if args.operation == "encrypt":
        result = rc4_encrypt(key, args.message.encode())
        print("Ciphertext:", result.hex())
    else:
        result = rc4_decrypt(key, bytes.fromhex(args.message))
        print("Decrypted text:", result.decode())

if __name__ == "__main__":
    main()
