import pandas as pd
from pathlib import Path 

# set path for a folder which containing the excel files
folder = Path(r"C:\Users\sachin chandra bhatt\Desktop\udemy_python\data\excel")

# loop excel files
for excel_file in folder.glob("*.xlsx"):
    try:
        hf = pd.read_excel(excel_file)
        csv_file = excel_file.with_suffix(".csv")
        hf.to_csv(csv_file, index=False)
        print(f"converted {excel_file.name} -> {csv_file.name}")
    except Exception as e:
        print(f"error converting {excel_file.name}: {e}")
# This code converts all Excel files in a specified folder to CSV format.
# It uses the pandas library to read the Excel files and save them as CSV files.
# The code handles exceptions that may occur during the conversion process and prints appropriate messages.
# The converted CSV files will have the same name as the original Excel files but with a .csv extension.
# Make sure to have the pandas library installed in your Python environment.