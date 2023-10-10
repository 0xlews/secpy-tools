import argparse
import base64
import re
import binascii  
import sys

# Ensure script is run with Python 3.10.4 or higher
if sys.version_info < (3, 10, 4):
    sys.exit("Script requires Python 3.10.4 or higher")

def is_valid_base64(s):
    """Check if a string is valid Base64 encoding."""
    pattern = re.compile(r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$')
    return bool(pattern.match(s))

def is_valid_hex(s):
    """Check if a string is valid Hexadecimal encoding."""
    pattern = re.compile(r'^[0-9a-fA-F]+$')
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
        
    encoded_strings_b64 = re.findall(pattern_b64, content)
    encoded_strings_hex = re.findall(pattern_hex, content)
        
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

    for encoded in encoded_strings_hex:
        encoded_str = encoded.decode('utf-8', 'ignore')
        if is_valid_hex(encoded_str) and encoded not in encoded_strings_b64:
            decoded = decode_hex(encoded_str)
            if decoded and decoded.strip() and is_readable_text(decoded):
                decoded_data.append((encoded_str, "Hexadecimal", decoded))
    
    return decoded_data

def main():
    """Main function to parse arguments and handle file I/O."""
    parser = argparse.ArgumentParser(description="Decode encoded strings in a file.")
    parser.add_argument("input", help="Path to the input file.")
    parser.add_argument("output", help="Path to the output file.")
    
    args = parser.parse_args()
    
    decoded_data = detect_and_decode(args.input)
    
    # Write the original string, its encoding method, and the decoded string to the output file
    with open(args.output, 'w', encoding='utf-8') as f:
        for original, encoding, data in decoded_data:
            f.write(f"{original}, {encoding}, {data}\n")

if __name__ == "__main__":
    main()
