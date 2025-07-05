import pandas as pd
from pathlib import Path

# set path for a folder which containing the csv files
folder = Path(r"C:\Users\sachin chandra bhatt\Desktop\udemy_python\csv")

# loop csv files
for csv_file in folder.glob("*.csv"):
    try:
        df = pd.read_csv(csv_file)
        excel_file = csv_file.with_suffix(".xlsx")
        df.to_excel(excel_file,index=False)
        print(f"converted {csv_file.name} -> {excel_file.name}")
    except Exception as e:
        print(f"error converting {csv_file.name}: {e}")


