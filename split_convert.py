import pandas as pd
import os

def split_excel_to_csv(excel_file_path, output_dir, lines_per_file=100000):
    """
    Splits an Excel file into multiple CSV files.

    Parameters:
    excel_file_path (str): The path of the Excel file.
    output_dir (str): The directory where CSV files will be saved.
    lines_per_file (int): Maximum number of lines per CSV file.
    """
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file_path, engine='openpyxl')

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Get the total number of rows
        total_rows = len(df)
        print(f"Total rows in the Excel file: {total_rows}")

        # Split the dataframe into chunks and save each chunk as a separate CSV file
        for start_row in range(0, total_rows, lines_per_file):
            end_row = min(start_row + lines_per_file, total_rows)
            chunk_df = df.iloc[start_row:end_row]
            csv_file_path = os.path.join(output_dir, f"part_{start_row//lines_per_file + 1}.csv")
            chunk_df.to_csv(csv_file_path, index=False)
            print(f"Saved {csv_file_path} with rows from {start_row} to {end_row-1}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    excel_file_path = r'path/to/your/file/list.xlsx'
    output_dir = r'path/to/folder/for/output'
    split_excel_to_csv(excel_file_path, output_dir)
