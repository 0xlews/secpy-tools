# CSV Data Tools

A collection of Python scripts to work with CSV data.

## Table of Contents

- [Append Data](#append-data)
- [Clean Data](#clean-data)
- [License](#license)

## Append Data

### Description

The `append.py` script allows you to merge two CSV files based on a common column and append a specified column from one file to another.

### Usage

You can use the `append.py` script to merge two CSV files and append a specified column. The script accepts the following options:

```bash
python append.py existing_file new_file --common_column "Description" --column_to_append "Oct-23" --output_file "merged_dataset.csv"
```

- `existing_file`: Path to the existing CSV file.
- `new_file`: Path to the new CSV file.
- `--common_column`: Common column to merge on (default: 'Description').
- `--column_to_append`: Name of the column to append from the new CSV file (e.g., 'Oct-23', default: 'Oct-23').
- `--output_file`: Path to the output merged CSV file (default: 'merged_dataset.csv').

[Read more](append.py)

## Clean Data

### Description

The `clean.py` script is used to clean a CSV file by filling missing values with empty strings.

### Usage

You can use the `clean.py` script to clean a CSV file by filling missing values with empty strings. The script accepts the following arguments:

```bash
python clean.py input_file output_file [--remove_duplicates]
```

- `input_file`: Path to the input CSV file.
- `output_file`: Path to the output cleaned CSV file.
- `--remove_duplicates`: (Optional) Remove duplicate rows and columns.

[Read more](clean.py)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

