import pandas as pd
import argparse

def clean_csv(input_file, output_file, remove_duplicates=True):
    try:
        # Check if the input file has a .csv extension
        if not input_file.endswith('.csv'):
            raise ValueError("Error: The input file must have a .csv extension.")

        df = pd.read_csv(input_file)

        # Fill missing values with an empty string
        df = df.fillna('')

        if remove_duplicates:
            # Remove duplicate rows
            df = df.drop_duplicates()

            # Remove duplicate columns
            df = df.loc[:, ~df.columns.duplicated()]#

        # Ensure the output file has a .csv extension
        if not output_file.endswith('.csv'):
            output_file += '.csv'

        df.to_csv(output_file, index=False)
        print(f"Cleaned data saved to {output_file}")

    except pd.errors.ParserError:
        print(f"Error: {input_file} is not a valid CSV file. Please provide a valid CSV file.")
    except ValueError as e:
        print(str(e))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Clean a CSV file by filling missing values with empty strings.")
    parser.add_argument('input_file', type=str, help="Path to the input CSV file")
    parser.add_argument('output_file', type=str, help="Path to the output cleaned CSV file. Will append .csv if not provided.")
    parser.add_argument('--remove_duplicates', action='store_true', help="Remove duplicate rows and columns")

    args = parser.parse_args()

    clean_csv(args.input_file, args.output_file, args.remove_duplicates)
