import os
import pandas as pd
import re

# Define the directory containing the Excel files
dir_path = 'Final_Extracted_Excels/'

# Define a function to extract the numerical data from a string
def extract_numeric_data(s):
    # Remove any non-numeric characters from the string
    s = re.sub(r'[^\d.]+', '', str(s))
    # Convert the string to a float and return it
    return float(s)

# Create an empty dataframe to store the results
df_output = pd.DataFrame(columns=['Sr_no', 'capex_total_y1', 'capex_total_y2','capex_total_y3','opex_total_y1','opex_total_y2','opex_total_y3'])

# Loop through each file in the directory
for filename in sorted(os.listdir(dir_path)):
    if filename.endswith('.xlsx'):
        # Construct the full file path
        file_path = os.path.join(dir_path, filename)

        try:
            # Read the Excel file into a pandas dataframe
            df = pd.read_excel(file_path, sheet_name='Financial Resources Utilised A')

            # Extract the numerical data from the relevant cells and sum it
            capex_total_y1 = df.iloc[3:7, 1].apply(extract_numeric_data).replace('-', 0).sum()
            capex_total_y2 = df.iloc[3:7, 2].apply(extract_numeric_data).replace('-', 0).sum()
            capex_total_y3 = df.iloc[3:7, 3].apply(extract_numeric_data).replace('-', 0).sum()
            opex_total_y1 = df.iloc[10:13, 1].apply(extract_numeric_data).replace('-', 0).sum()
            opex_total_y2 = df.iloc[10:13, 2].apply(extract_numeric_data).replace('-', 0).sum()
            opex_total_y3 = df.iloc[10:13, 3].apply(extract_numeric_data).replace('-', 0).sum()

            # Add a new row with the patent_grant and patent_published values, along with the file's serial number
            sr_no = int(filename.split('.')[0])
            df_output = df_output.append({'Sr_no': sr_no, 'capex_total_y1': capex_total_y1,'capex_total_y2': capex_total_y2,'capex_total_y3': capex_total_y3,'opex_total_y1': opex_total_y1,'opex_total_y2': opex_total_y2,'opex_total_y3': opex_total_y3}, ignore_index=True)
        except ValueError:
            print(f"Skipping file {filename}: Worksheet not found.")

# Save the dataframe as an Excel file named "FRU.xlsx"
df_output.to_excel('FRU.xlsx', index=False)

print("File saved successfully!")