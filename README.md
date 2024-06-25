### README

### Excel to CSV Converter

This Python application converts an Excel file into multiple CSV files, splitting the data into manageable chunks to facilitate importing into Google Sheets or other applications with file size limitations.

### Features

- Converts Excel files (.xlsx) to CSV files.
- Splits data into multiple CSV files if the row count exceeds a specified limit (default: 100,000 lines).
- Ensures smooth handling of large datasets.

### Requirements

- Python 3.x
- pandas
- openpyxl

### Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   .\venv\Scripts\activate  # Windows
   ```
4. Install the required packages:
   ```
   pip install pandas openpyxl
   ```

## Usage

1. Place your Excel file in the project directory.
2. Update the `excel_file_path` and `output_dir` variables in the `split_convert.py` script with the appropriate file paths.
3. Run the script:
   ```
   python split_convert.py
   ```
4. The script will generate multiple CSV files in the specified output directory, each containing a maximum of 100,000 lines (or the specified limit).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
