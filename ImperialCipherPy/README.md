
# ImperialCipherPy

ImperialCipherPy is a Python tool for encrypting and decrypting messages using the Caesar cipher, a simple but historically significant encryption technique. Named after Julius Caesar, who famously used it in his private correspondence, this tool brings an ancient cipher to the modern digital age.

## Features

- Encrypt and decrypt text using the Caesar cipher algorithm.
- Simple command-line interface for easy operation.
- Versatile for educational purposes or basic encryption needs.

## Usage

1. Ensure you have Python installed on your system.

2. Download and save the `imperial_cipher.py` script.

3. For usage, execute `imperial_cipher.py`.

4. To encrypt a message:
   ```
   python imperial_cipher.py -e -t "Your Message" -s <Shift Value>
   ```

5. To decrypt a message:
   ```
   python imperial_cipher.py -d -t "Encrypted Message" -s <Shift Value>
   ```

## Examples

- Encrypting "HELLO" with a shift of 3:
  ```
  python imperial_cipher.py -e -t "HELLO" -s 3
  ```
  Output: "KHOOR"

- Decrypting "KHOOR" with a shift of 3:
  ```
  python imperial_cipher.py -d -t "KHOOR" -s 3
  ```
  Output: "HELLO"

## Contributing

Contributions to ImperialCipherPy are welcome. Please ensure to follow the contribution guidelines provided in CONTRIBUTING.md.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
