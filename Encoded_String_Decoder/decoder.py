import argparse
import base64
import re
import binascii  
import sys
import urllib.parse
import csv
import os
import json

# Ensure script is run with Python 3.10.4 or higher
if sys.version_info < (3, 10, 4):
    sys.exit("Script requires Python 3.10.4 or higher")

def is_valid_base64(s):
    """Check if a string is valid Base64 encoding."""
    pattern = re.compile(r'^(?:%[0-9a-fA-F]{2}|[A-Za-z0-9_.~!$&\'()*+,;=:@/-])+$')
    return bool(pattern.match(s))

def is_valid_hex(s):
    """Check if a string is valid Hexadecimal encoding."""
    pattern = re.compile(r'^[0-9a-fA-F]+$')
    return bool(pattern.match(s))

def is_valid_url(s):
    """Check if a string may be URL-encoded."""
    # Pattern looks for '%' followed by two hexadecimal digits.
    pattern = re.compile(r'(?:%[0-9a-fA-F]{2}|[A-Za-z0-9_.~!$&\'()*+,;=:@/-])+')
    return bool(pattern.match(s))


def decode_hex(s):
    """Try to decode a hexadecimal string into utf-8, return None if unsuccessful."""
    try:
        return bytes.fromhex(s).decode('utf-8')
    except (ValueError, binascii.Error, UnicodeDecodeError):
        return None 

def is_readable_text(s):
    """Check if a string seems to be readable text by ensuring 95% or more characters are printable."""
    threshold = 0.95  
    total_chars = len(s)
    printable_chars = sum(1 for c in s if c.isprintable())
    ratio = printable_chars / total_chars
    return ratio > threshold

def detect_and_decode(file_path):
    """
    Detect and decode encoded strings within a given file.
    
    Args:
        file_path (str): Path to the file to be analyzed.

    Returns:
        list: A list of tuples containing original encoded string, encoding type, and decoded string.
    """
    with open(file_path, 'rb') as f:
        content = f.read()
        
    pattern_b64 = rb'(?:[A-Za-z0-9+/]{4}){2,}(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?'
    pattern_hex = rb'[0-9a-fA-F]+'
    pattern_url = rb'(?:%[0-9a-fA-F]{2}|[A-Za-z0-9_.~!$&\'()*+,;=:@/-])+'

        
    encoded_strings_b64 = re.findall(pattern_b64, content)
    encoded_strings_hex = re.findall(pattern_hex, content)
    encoded_strings_url = re.findall(pattern_url, content)
        
    decoded_data = []

    for encoded in encoded_strings_b64:
        encoded_str = encoded.decode('utf-8', 'ignore')
        if is_valid_base64(encoded_str):
            try:
                decoded = base64.b64decode(encoded).decode('utf-8')
                if decoded.strip() and is_readable_text(decoded):  
                    decoded_data.append((encoded_str, "Base64", decoded))
            except:
                pass 

    MIN_HEX_LENGTH = 4  # minimal length to reduce noise

    for encoded in encoded_strings_hex:
        encoded_str = encoded.decode('utf-8', 'ignore')
        if is_valid_hex(encoded_str) and len(encoded_str) >= MIN_HEX_LENGTH and encoded not in encoded_strings_b64:
            decoded = decode_hex(encoded_str)
            if decoded and decoded.strip() and is_readable_text(decoded):
                decoded_data.append((encoded_str, "Hexadecimal", decoded))


    for encoded in encoded_strings_url:
        encoded_str = encoded.decode('utf-8', 'ignore')
        try:
            # Additional checks to be more confident that it is really URL encoded data
            if "%" in encoded_str and encoded_str not in [e[0] for e in decoded_data]:
                decoded = urllib.parse.unquote(encoded_str)
                if decoded.strip() and is_readable_text(decoded):
                    decoded_data.append((encoded_str, "URL Encoding", decoded))
        except:
            pass
    
    return decoded_data

def main():
    """Main function to parse arguments and handle file I/O."""
    parser = argparse.ArgumentParser(description="Decode encoded strings in a file.")
    parser.add_argument("input", help="Path to the input file.")
    parser.add_argument("output", help="Path to the output file.")
    
    args = parser.parse_args()
    
    # Ensure the output file has a valid extension and get output format
    output_file_path, ext = os.path.splitext(args.output)
    if not ext or ext.lower() not in ['.csv', '.json']:
        sys.exit("Output file must have a valid extension (.csv or .json).")
    
    # Get decoded data
    decoded_data = detect_and_decode(args.input)
    
    # Output to CSV
    if ext.lower() == '.csv':
        with open(args.output, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Encoded String", "Encoding Type", "Decoded String"])  # header
            writer.writerows(decoded_data)  # data rows
    
    # Output to JSON
    elif ext.lower() == '.json':
        json_data = [
            {"Encoded String": enc, "Encoding Type": enc_type, "Decoded String": dec}
            for enc, enc_type, dec in decoded_data
        ]
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
