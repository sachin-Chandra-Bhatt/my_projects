# merge and clean excel files

import pandas as pd
from pathlib import Path

folder_path = Path(r'C:\Users\sachin chandra bhatt\Desktop\udemy_python\new')
output_file = folder_path / 'merged_cleaned_data.xlsx'

# read and merge excel files
all_files = []
for file in folder_path.glob('*.xlsx'):
    print(f'Reading {file}')
    df = pd.read_excel(file)
    all_files.append(df)


# Concatenate all dataframes
merged_df = pd.concat(all_files, ignore_index=True)

# remove all blank rows
merged_df.dropna(how='all', inplace=True)


# remove duplicate rows
merged_df.drop_duplicates(inplace=True)

# check the data types of the columns
print("\nData Types of Columns:")
print(merged_df.dtypes)

# save the cleaned data to a new excel file
merged_df.to_excel(output_file, index=False)
print(f"\nMerged and cleaned data saved to {output_file}")

# Display the first few rows of the cleaned data
print("\nFirst few rows of the cleaned data:")
print(merged_df.head())