# Encoded String Decoder

Encoded String Decoder is a simple Python utility designed meticulously to decode obscured content within files. Utilizing regex pattern recognition techniques, it scans through a file to identify strings potentially encrypted using Base64 and Hexadecimal encoding methods, decodes them, and conveniently outputs the original encoded string, encoding method, and the decoded string.

## Table of Contents

- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Built With](#built-with)
- [License](#license)

## Getting Started

### Requirements

- Python 3.10.4 or higher
- Additional packages may be specified in `requirements.txt`

### Installation

Clone the repository
   ```sh
  git clone https://github.com/lewiswigmore/python-tools.git
  ```
## Usage
   ```sh
  python decoder.py INPUT_FILE OUTPUT_FILE [-e ENCODING]
  ```
- INPUT_FILE: Path to the file containing the encoded strings.
- OUTPUT_FILE: Path to the file where the decoded data will be written, with a valid extension (.csv or .json).
- ENCODING (optional): The encoding method to detect ("Base64", "Hexadecimal", or "URL Encoding"). If omitted, all encoding methods are used.

## Functionality

- Detect and Decode Various Encoded Strings: This tool identifies potential Base64, Hexadecimal, and URL-encoded strings using regular expressions and decodes them, considering validation to ensure accurate decoding.
- Selective Decoding: The tool allows users to specify which encoding method should be used, providing the flexibility to focus on specific types of encoded strings.
- Output Formats: Decoded data can be outputted in two formats: CSV or JSON, giving users the option to work with the data in different contexts.
- Prevent Duplicate Decoding: Ensures that if a Hexadecimal string is also valid Base64, it\'s not decoded twice.

## Built With

Python 3.10.4


## License

Distributed under the MIT License. See LICENSE for more information.

