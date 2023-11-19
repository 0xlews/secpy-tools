
"""
 __ _            _   _       ___       
/ _\ | ___ _   _| |_| |__   / _ \_   _ 
\ \| |/ _ \ | | | __| '_ \ / /_)/ | | |
_\ \ |  __/ |_| | |_| | | / ___/| |_| |
\__/_|\___|\__,_|\__|_| |_\/     \__, |
                                 |___/ 
"""

import argparse
import base64
import binascii
import csv
import os
import re
import sys
import urllib.parse
import json

# Ensure Python version compatibility
if sys.version_info < (3, 10, 4):
    sys.exit("Requires Python 3.10.4 or higher")

# Function to check if a string is valid base64
def is_valid_base64(s):
    pattern = re.compile(r'^(?:%[0-9a-fA-F]{2}|[A-Za-z0-9_.~!$&\'()*+,;=:@/-])+$')
    return bool(pattern.match(s))

# Function to check if a string is valid hexadecimal
def is_valid_hex(s):
    pattern = re.compile(r'^[0-9a-fA-F]+$')
    return bool(pattern.match(s))

# Function to check if a string is valid URL encoding
def is_valid_url(s):
    pattern = re.compile(r'(?:%[0-9a-fA-F]{2}|[A-Za-z0-9_.~!$&\'()*+,;=:@/-])+')
    return bool(pattern.match(s))

# Function to decode a hexadecimal string
def decode_hex(s):
    try:
        return bytes.fromhex(s).decode('utf-8')
    except (ValueError, binascii.Error, UnicodeDecodeError):
        return None

# Function to determine if a string is mostly readable text
def is_readable_text(s):
    threshold = 0.95
    total_chars = len(s)
    printable_chars = sum(1 for c in s if c.isprintable())
    ratio = printable_chars / total_chars
    return ratio > threshold

# Function to detect and decode encoded strings in a file
def detect_and_decode(file_path, encoding=None):
    with open(file_path, 'rb') as f:
        content = f.read()

    # Define regular expressions for different types of encodings
    pattern_b64 = rb'(?:[A-Za-z0-9+/]{4}){2,}(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?'
    pattern_hex = rb'[0-9a-fA-F]+'
    pattern_url = rb'(?:%[0-9a-fA-F]{2}|[A-Za-z0-9_.~!$&\'()*+,;=:@/-])+'

    # Find encoded strings matching the regular expressions
    encoded_strings_b64 = re.findall(pattern_b64, content)
    encoded_strings_hex = re.findall(pattern_hex, content)
    encoded_strings_url = re.findall(pattern_url, content)

    decoded_data = []

    if encoding in [None, "Base64"]:
        for encoded in encoded_strings_b64:
            encoded_str = encoded.decode('utf-8', 'ignore')
            if is_valid_base64(encoded_str):
                try:
                    decoded = base64.b64decode(encoded).decode('utf-8')
                    if decoded.strip() and is_readable_text(decoded):
                        decoded_data.append((encoded_str, "Base64", decoded))
                except:
                    pass

    MIN_HEX_LENGTH = 4

    if encoding in [None, "Hexadecimal"]:
        for encoded in encoded_strings_hex:
            encoded_str = encoded.decode('utf-8', 'ignore')
            if is_valid_hex(encoded_str) and len(encoded_str) >= MIN_HEX_LENGTH and encoded not in encoded_strings_b64:
                decoded = decode_hex(encoded_str)
                if decoded and decoded.strip() and is_readable_text(decoded):
                    decoded_data.append((encoded_str, "Hex", decoded))

    if encoding in [None, "URL Encoding"]:
        for encoded in encoded_strings_url:
            encoded_str = encoded.decode('utf-8', 'ignore')
            try:
                if "%" in encoded_str and encoded_str not in [e[0] for e in decoded_data]:
                    decoded = urllib.parse.unquote(encoded_str)
                    if decoded.strip() and is_readable_text(decoded):
                        decoded_data.append((encoded_str, "URL Encoding", decoded))
            except:
                pass

    return decoded_data

# Main function to handle command-line arguments and execute the program
def main():
    parser = argparse.ArgumentParser(description="Decode encoded strings in a file")
    parser.add_argument("-i", "--input", help="Input file path")
    parser.add_argument("-o", "--output", help="Output file path")
    parser.add_argument(
        "-e", "--encoding",
        choices=["Base64", "Hex", "URL Encoding"],
        help="Specify the encoding method to detect (default: all)"
    )

    args = parser.parse_args()

    # Check if no arguments were provided
    if len(sys.argv) == 1:
        print(__doc__)  # Print ASCII art
        parser.print_help()  # Print help message
        sys.exit(1)  # Exit the script

    # Check the output file extension
    output_file_path, ext = os.path.splitext(args.output)
    if not ext or ext.lower() not in ['.csv', '.json']:
        sys.exit("Output file must have a valid extension (.csv or .json)")

    decoded_data = detect_and_decode(args.input, args.encoding)

    if ext.lower() == '.csv':
        with open(args.output, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Encoded String", "Encoding Type", "Decoded String"])
            writer.writerows(decoded_data)

    elif ext.lower() == '.json':
        json_data = [
            {"Encoded String": enc, "Encoding Type": enc_type, "Decoded String": dec}
            for enc, enc_type, dec in decoded_data
        ]
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
