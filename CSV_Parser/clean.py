import pandas as pd
import argparse

def clean_csv(input_file, output_file, remove_duplicates=True):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Fill missing values with an empty string 
    df = df.fillna('')

    if remove_duplicates:
        # Remove duplicate rows
        df = df.drop_duplicates()

        # Remove duplicate columns
        df = df.loc[:, ~df.columns.duplicated()]

    # Save the cleaned data to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Clean a CSV file by filling missing values with empty strings.")
    parser.add_argument('input_file', type=str, help="Path to the input CSV file")
    parser.add_argument('output_file', type=str, help="Path to the output cleaned CSV file")
    parser.add_argument('--remove_duplicates', action='store_true', help="Remove duplicate rows and columns")

    args = parser.parse_args()

    clean_csv(args.input_file, args.output_file, args.remove_duplicates)
