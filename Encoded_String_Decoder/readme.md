# Encoded String Decoder

Encoded String Decoder is a simple Python utility designed meticulously to decode obscured content within files. Utilizing regex pattern recognition techniques, it scans through a file to identify strings potentially encrypted using Base64 and Hexadecimal encoding methods, decodes them, and conveniently outputs the original encoded string, encoding method, and the decoded string.

## Table of Contents

- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Built With](#built-with)
- [Contribution](#contribution)
- [License](#license)

## Getting Started

### Requirements

- Python 3.10.4 or higher
- Additional packages may be specified in `requirements.txt`

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/lewiswigmore/python-tools.git

## Usage

python decoder.py [INPUT_FILE] [OUTPUT_FILE]

## Functionality

Detect and Decode Base64 Strings: This tool identifies potential Base64 strings using a regular expression and decodes them, considering validation to ensure accurate decoding.

Detect and Decode Hexadecimal Strings: Similarly, it identifies and decodes Hexadecimal strings.

Prevent Duplicate Decoding: Ensures that if a Hexadecimal string is also valid Base64, it's not decoded twice.

## Built With

Python 3.10.4

## Contribution

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

## License

Distributed under the MIT License. See LICENSE for more information.


