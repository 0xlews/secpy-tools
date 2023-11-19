
"""
 _______  ______ _     _ _     _       _ _  
(_______)/ _____|_)   (_|_)   (_)  _  (_) | 
 _      ( (____  _     _ _     _ _| |_ _| | 
| |      \____ \| |   | | |   | (_   _) | | 
| |_____ _____) )\ \ / /| |___| | | |_| | | 
 \______|______/  \___/  \_____/   \__)_|\_)
 """

import pandas as pd
import argparse
import sys

# Function to merge and append CSV files
def merge_csv_files(existing_file, new_file, common_column, column_to_append):
    existing_dataset = pd.read_csv(existing_file)
    new_dataset = pd.read_csv(new_file)
    merged_dataset = pd.merge(existing_dataset, new_dataset, on=common_column, how='left')
    merged_dataset[column_to_append] = new_dataset[column_to_append]
    return merged_dataset

# Function to clean CSV files
def clean_csv(input_file, output_file, remove_duplicates=True):
    df = pd.read_csv(input_file)
    df = df.fillna('')
    if remove_duplicates:
        df = df.drop_duplicates()
    df.to_csv(output_file, index=False)

# Argument parsing
parser = argparse.ArgumentParser(description="CSVUtil - A utility tool for CSV data manipulation")
parser.add_argument("--merge", help="Merge two CSV files", action="store_true")
parser.add_argument("--clean", help="Clean a CSV file", action="store_true")
parser.add_argument("--input", help="Input CSV file", type=str)
parser.add_argument("--output", help="Output CSV file", type=str)
parser.add_argument("--existing", help="Existing CSV file for merging", type=str)
parser.add_argument("--new", help="New CSV file to merge", type=str)
parser.add_argument("--common", help="Common column for merging", type=str)
parser.add_argument("--append", help="Column to append in merging", type=str)

args = parser.parse_args()

# Check if no arguments were provided
if len(sys.argv) == 1:
    print(__doc__)  # Print ASCII art
    parser.print_help()  # Print help message
    sys.exit(1)  # Exit the script

# Executing the specified functionality
if args.merge:
    if not all([args.existing, args.new, args.common, args.append]):
        print("Error: Missing arguments for merging")
        sys.exit(1)
    merged_data = merge_csv_files(args.existing, args.new, args.common, args.append)
    merged_data.to_csv(args.output if args.output else "merged_output.csv", index=False)
    print("Merge completed. Output saved to", args.output if args.output else "merged_output.csv")

elif args.clean:
    if not args.input:
        print("Error: Missing input file for cleaning")
        sys.exit(1)
    clean_csv(args.input, args.output if args.output else "cleaned_output.csv")
    print("Cleaning completed. Output saved to", args.output if args.output else "cleaned_output.csv")
