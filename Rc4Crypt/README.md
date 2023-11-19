```
░█▀▄░█▀▀░█░█░█▀▀░█▀▄░█░█░█▀█░▀█▀
░█▀▄░█░░░░▀█░█░░░█▀▄░░█░░█▀▀░░█░
░▀░▀░▀▀▀░░░▀░▀▀▀░▀░▀░░▀░░▀░░░░▀░
```
The `rc4crypt.py` script is a simple command-line tool that allows you to encrypt and decrypt messages using the RC4 (Rivest Cipher 4) stream cipher. It uses the PyCryptodome library to perform the encryption and decryption operations. This tool is designed for educational purposes and provides a straightforward interface for experimenting with the RC4 algorithm.

## Usage

### Installation

Before using the script, you need to install the required library, PyCryptodome. You can install it using pip:

```
pip install pycryptodome
```

### Running the Script

To use the script, run it from the command line, providing the following arguments:

1. `operation`: Specify whether you want to "encrypt" or "decrypt" a message.
2. `key`: Enter the encryption/decryption key as a string.
3. `message`: Provide the message you want to encrypt or the ciphertext for decryption.

#### Encryption Example

To encrypt a message, use the following command:

```
python rc4crypt.py encrypt YourSecretKey "This is a secret message"
```

#### Decryption Example

To decrypt a message, use the following command:

```
python rc4crypt.py decrypt YourSecretKey CiphertextString
```

Replace `YourSecretKey` with your actual encryption key, and `CiphertextString` with the ciphertext you want to decrypt.

## Security Note

Please note that the RC4 cipher is considered insecure for modern cryptographic purposes due to vulnerabilities. This tool is for educational purposes and should not be used for sensitive or production-level encryption. It's recommended to use stronger encryption methods for security-critical applications.

## License

This script is provided under the [MIT License](LICENSE).
