# Caesar Cipher Decryption Script

This Python script allows you to decrypt a message that has been encrypted using a Caesar cipher with a specific shift value. It provides a simple command-line interface to perform the decryption.

## Usage

To use this script, follow these steps:

1. Ensure you have Python installed on your system.

2. Save the provided script to a Python file, for example, `caesar_decryption.py`.

3. Open your terminal or command prompt.

4. Run the script with the `-t` or `--text` argument, followed by the encrypted text you want to decrypt. For example:

   ```bash
   python caesar_decryption.py -t "Xli wlsyph fiwx jymw mr gsqtpegx."
   ```

   Replace `"Xli wlsyph fiwx jymw mr gsqtpegx."` with the encrypted text you want to decrypt.

5. The script will then display the decrypted text for all possible shift values (0 to 25). The output will look something like this:

   ```
   Shift 0: The secret text is "decrypting."
   Shift 1: Sgd rdbnfs sdbn hrln lq fcpsofdgw.
   Shift 2: Rfc qcamer rcam gqkm kp eborncefv.
   ...
   ```

   Each line shows the decrypted text for a specific shift value.

## How It Works

The script works by trying all possible shift values (0 to 25) and decrypting the text for each shift. It recognizes and preserves non-alphabetic characters, so they remain unchanged in the decrypted text.

## License

This script is provided under the [MIT License](LICENSE), which allows you to use and modify it for your needs.

Please feel free to modify and adapt this script to suit your specific requirements, and don't hesitate to reach out if you have any questions or need further assistance. 