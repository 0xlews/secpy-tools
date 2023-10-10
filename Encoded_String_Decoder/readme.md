# Encoded String Decoder

A simple Python utility that scans a given file for potential Base64 and Hexadecimal encoded strings and decodes them. 

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Built With](#built-with)
- [Contribution](#contribution)
- [License](#license)

## Getting Started

### Prerequisites

- Python 3.x
- Basic knowledge of command-line operations

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/[YourUsername]/EncodedStringDecoder.git

## Usage

python decoder.py [INPUT_FILE] [OUTPUT_FILE]

## Functionality

Detect and Decode Base64 Strings: This tool identifies potential Base64 strings using a regular expression and decodes them, considering validation to ensure accurate decoding.

Detect and Decode Hexadecimal Strings: Similarly, it identifies and decodes Hexadecimal strings.

Prevent Duplicate Decoding: Ensures that if a Hexadecimal string is also valid Base64, it's not decoded twice.

## Built With

Python 3

## Contribution

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request

## License

Distributed under the MIT License. See LICENSE for more information.


