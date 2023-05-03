import os
import pandas as pd

# Define the directory containing the Excel files
dir_path = 'Extracted Excels/'

# Create an empty dataframe to store the results
df_output = pd.DataFrame(columns=['Sr_no', 'total_fundedbyinsti'])

# Loop through each file in the directory
for filename in sorted(os.listdir(dir_path)):
    if filename.endswith('.xlsx'):
        # Construct the full file path
        file_path = os.path.join(dir_path, filename)

        try:
            # Read the Excel file into a pandas dataframe
            df = pd.read_excel(file_path, sheet_name='Total Actual Student Strength ')

            total_fundedbyinsti = df.iloc[:, 10].replace('-', 0).astype(float).sum()

            # Add a new row with the patent_grant and patent_published values, along with the file's serial number
            sr_no = int(filename.split('.')[0])
            df_output = df_output.append({'Sr_no': sr_no, 'total_fundedbyinsti': total_fundedbyinsti}, ignore_index=True)

        except ValueError:
            print(f"Skipping file {filename}: Worksheet not found.")

# Save the dataframe as an Excel file named "IPR.xlsx"
df_output.to_excel('ESCS.xlsx', index=False)

print("File saved successfully!")