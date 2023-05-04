import os
import pandas as pd

# Define the directory containing the Excel files
dir_path = 'Extracted Excels/'

# Create an empty dataframe to store the results
df_output = pd.DataFrame(columns=['Sr_no', 'capex_total_y1', 'capex_total_y2','capex_total_y3','opex_total_y1','opex_total_y2','opex_total_y3'])

# Loop through each file in the directory
for filename in sorted(os.listdir(dir_path)):
    if filename.endswith('.xlsx'):
        # Construct the full file path
        file_path = os.path.join(dir_path, filename)

        try:
            # Read the Excel file into a pandas dataframe
            df = pd.read_excel(file_path, sheet_name= 'Financial Resources Utilised A')

            capex_total_y1 = df.iloc[3:7, 1].replace('-', 0).astype(float).sum()
            capex_total_y2 = df.iloc[3:7, 2].replace('-', 0).astype(float).sum()
            capex_total_y3 = df.iloc[3:7, 3].replace('-', 0).astype(float).sum()
            opex_total_y1 = df.iloc[10:13, 1].replace('-', 0).astype(float).sum()
            opex_total_y2 = df.iloc[10:13, 2].replace('-', 0).astype(float).sum()
            opex_total_y3 = df.iloc[10:13, 3].replace('-', 0).astype(float).sum()
            # sum_b = df.iloc[3:7, 1].sum()
            # total_sanc_intake_y2 = df.iloc[:, 2].replace('-', 0).astype(float).sum()
            # total_sanc_intake_y3 = df.iloc[:, 3].replace('-', 0).astype(float).sum()
            # total_sanc_intake_y4 = df.iloc[:, 4].replace('-', 0).astype(float).sum()

            # Add a new row with the patent_grant and patent_published values, along with the file's serial number
            sr_no = int(filename.split('.')[0])
            df_output = df_output.append({'Sr_no': sr_no, 'capex_total_y1': capex_total_y1,'capex_total_y2': capex_total_y2,'capex_total_y3': capex_total_y3,'opex_total_y1': opex_total_y1,'opex_total_y2': opex_total_y2,'opex_total_y3': opex_total_y3}, ignore_index=True)
        except ValueError:
            print(f"Skipping file {filename}: Worksheet not found.")

# Save the dataframe as an Excel file named "IPR.xlsx"
df_output.to_excel('FRU.xlsx', index=False)

print("File saved successfully!")