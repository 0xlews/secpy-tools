```
 __ _            _   _       ___       
/ _\ | ___ _   _| |_| |__   / _ \_   _ 
\ \| |/ _ \ | | | __| '_ \ / /_)/ | | |
_\ \ |  __/ |_| | |_| | | / ___/| |_| |
\__/_|\___|\__,_|\__|_| |_\/     \__, |
                                 |___/ 
```

SleuthPy is a Python utility designed to decode obscured content within files. Utilising regex pattern recognition techniques, it scans through a file to identify strings potentially encoded using Base64, Hexadecimal, and URL encoding methods. It decodes them and outputs the original encoded string, the encoding method, and the decoded string.

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

### Installation

Clone the repository:

`git clone https://github.com/lewiswigmore/sleuthpy.git`

## Usage

Run SleuthPy using the following command:

`python sleuth.py --input INPUT_FILE --output OUTPUT_FILE [-e ENCODING]`

- **--input INPUT_FILE**: Specify the path to the file containing the encoded strings.
- **--output OUTPUT_FILE**: Define the path to the file where the decoded data will be written. The output file must have a valid extension (.csv or .json).
- **-e, --encoding ENCODING** (optional): Choose the encoding method to detect ("Base64", "Hexadecimal", or "URL Encoding"). If this option is omitted, all encoding methods are used.

### Examples

#### Detecting All Encodings

`python sleuth.py --input example.txt --output results.csv`

This command scans `example.txt` for all supported encoding types and outputs the decoded data in `results.csv`.

#### Specific Encoding Detection

`python sleuth.py --input example.txt --output results.json -e Base64`

In this example, `sleuth.py` will only look for Base64 encoded strings in `example.txt` and save the decoded results in `results.json`.

## Functionality

- **Detect and Decode Various Encoded Strings**: Identifies potential Base64, Hexadecimal, and URL-encoded strings and decodes them accurately.
- **Selective Decoding**: Allows specifying the encoding method, providing flexibility to focus on specific types of encoded strings.
- **Output Formats**: Supports CSV or JSON for output, catering to different user needs.
- **Efficient Decoding**: Avoids duplicate decoding of strings valid in multiple formats.

## Built With

- Python 3.10.4

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
