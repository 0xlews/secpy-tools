import argparse
import base64
import re
import binascii  

# Check if a string is valid Base64
def is_valid_base64(s):
    pattern = re.compile(r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$')
    return bool(pattern.match(s))

# Check if a string is valid Hexadecimal
def is_valid_hex(s):
    pattern = re.compile(r'^[0-9a-fA-F]+$')
    return bool(pattern.match(s))

# Decode a hexadecimal string into utf-8 if possible
def decode_hex(s):
    try:
        return bytes.fromhex(s).decode('utf-8')
    except (ValueError, binascii.Error, UnicodeDecodeError):
        return None 

def is_readable_text(s):
    """
    Check if a string seems to be readable text.
    :param s: String to check.
    :return: Boolean indicating whether the string seems to be readable text.
    """
    # Define a threshold for which percentage of characters must be printable
    threshold = 0.95  # 95%
    # Get the total length of the string
    total_chars = len(s)
    # Get the number of printable characters in the string
    printable_chars = sum(1 for c in s if c.isprintable())
    # Calculate the ratio of printable characters to total characters
    ratio = printable_chars / total_chars
    # Return whether the ratio exceeds the defined threshold
    return ratio > threshold

# Detect and decode encoded strings within a given file
def detect_and_decode(file_path):
    """
    Detect and decode encoded strings within a given file.

    Args:
        file_path (str): Path to the file to be analyzed.

    Returns:
        list: A list of decoded strings found in the file.
    """

    with open(file_path, 'rb') as f:
        content = f.read()
        
    pattern_b64 = rb'(?:[A-Za-z0-9+/]{4}){2,}(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?'
    pattern_hex = rb'[0-9a-fA-F]+'
        
    encoded_strings_b64 = re.findall(pattern_b64, content)
    encoded_strings_hex = re.findall(pattern_hex, content)
        
    # Use a set to store decoded strings, this helps in avoiding duplicates.
    decoded_data = set()
        
    # Iterate over all potential Base64 encoded strings found.
    for encoded in encoded_strings_b64:
        # Decode the bytes to string ignoring non-utf-8 chars.
        encoded_str = encoded.decode('utf-8', 'ignore')
        # Check if the string is valid Base64.
        if is_valid_base64(encoded_str):
            try:
                # Try decoding the Base64 string and if it's readable, add to the set.
                decoded = base64.b64decode(encoded).decode('utf-8')
                if decoded.strip() and is_readable_text(decoded):  
                    decoded_data.add(decoded)
            except:
                pass 
    
    # Iterate over all potential Hexadecimal encoded strings found.
    for encoded in encoded_strings_hex:
        encoded_str = encoded.decode('utf-8', 'ignore')
        if is_valid_hex(encoded_str) and encoded not in encoded_strings_b64:
            decoded = decode_hex(encoded_str)
            if decoded and decoded.strip() and is_readable_text(decoded):
                decoded_data.add(decoded)               
    return decoded_data     

# Main function to execute the script
def main():
    # Define argument parser and arguments
    parser = argparse.ArgumentParser(description="Decode encoded strings in a file.")
    parser.add_argument("input", help="Path to the input file.")
    parser.add_argument("output", help="Path to the output file.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Decode strings found in the input file
    decoded_data = detect_and_decode(args.input)
    
    # Write the decoded data to the output file
    with open(args.output, 'w', encoding='utf-8') as f:
        for data in decoded_data:
            f.write(data + '\n')

# Execute the main function if the script is run as the main module
if __name__ == "__main__":
    main()