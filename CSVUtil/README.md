
```
 _______  ______ _     _ _     _       _ _  
(_______)/ _____|_)   (_|_)   (_)  _  (_) | 
 _      ( (____  _     _ _     _ _| |_ _| | 
| |      \____ \| |   | | |   | (_   _) | | 
| |_____ _____) )\ \ / /| |___| | | |_| | | 
 \______|______/  \___/  \_____/   \__)_|\_)
 ```

# CSVUtil

Welcome to CSVUtil, a versatile Python utility for manipulating CSV files. This tool currently combines functionalities for both merging and cleaning CSV data.

## Features

- **Merge CSV Files**: Merge two CSV files based on a common column. This feature allows you to append a specific column from one CSV file to another.
- **Clean CSV Files**: Clean a CSV file by removing duplicates and filling in missing values.

## Getting Started

### Prerequisites

- Python 3.x
- Pandas library

### Installation

Ensure you have Python and Pandas installed on your system. You can install Pandas using pip if it's not already installed:

```
pip install pandas
```

### Usage

#### Merging CSV Files

To merge two CSV files, use the following command:

```
python CSVUtil.py --merge --existing [existing_file.csv] --new [new_file.csv] --common [common_column] --append [column_to_append] --output [output_file.csv]
```

- `existing_file.csv`: The CSV file that you want to merge another file into.
- `new_file.csv`: The new CSV file to merge.
- `common_column`: The common column based on which the merge will happen.
- `column_to_append`: The column from the new file that you want to append to the existing file.
- `output_file.csv`: The name of the output file (optional).

#### Cleaning CSV Files

To clean a CSV file, use the following command:

```
python CSVUtil.py --clean --input [input_file.csv] --output [output_file.csv]
```

- `input_file.csv`: The CSV file that you want to clean.
- `output_file.csv`: The name of the cleaned output file (optional).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.