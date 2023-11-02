import pandas as pd
import argparse

def merge_csv_files(existing_file, new_file, common_column, column_to_append):
    existing_dataset = pd.read_csv(existing_file)
    new_dataset = pd.read_csv(new_file)

    # Merge the datasets based on the common column, preserving all rows from the left dataset
    merged_dataset = pd.merge(existing_dataset, new_dataset, on=common_column, how='left')

    # Append the specified column to the merged dataset
    merged_dataset[column_to_append] = new_dataset[column_to_append]

    # Sort the DataFrame based on the "Description" column
    merged_dataset = merged_dataset.sort_values(by='Description')

    return merged_dataset

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Merge two CSV files based on a common column and append a specified column.")
    parser.add_argument('existing_file', type=str, help="Path to the existing CSV file")
    parser.add_argument('new_file', type=str, help="Path to the new CSV file")
    parser.add_argument('--common_column', type=str, default='Description', help="Common column to merge on (default: 'Description')")
    parser.add_argument('--column_to_append', type=str, default='Oct-23', help="Name of the column to append from the new CSV file (e.g., 'Oct-23')")
    parser.add_argument('--output_file', type=str, default='merged_dataset.csv', help="Path to the output merged CSV file (default: 'merged_dataset.csv')")

    args = parser.parse_args()

    merged_dataset = merge_csv_files(args.existing_file, args.new_file, args.common_column, args.column_to_append)
    merged_dataset.to_csv(args.output_file, index=False)
    print(f"Merged dataset saved to {args.output_file}")
