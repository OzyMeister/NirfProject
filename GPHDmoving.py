import os
import pandas as pd

# Define the directory containing the Excel files
dir_path = 'Extracted Excels/'

# Create an empty dataframe to store the results
df_output = pd.DataFrame(columns=['Sr_no', 'tot_phd_full_grad', 'tot_phd_part_grad'])

# Loop through each file in the directory
for filename in sorted(os.listdir(dir_path)):
    if filename.endswith('.xlsx'):
        # Construct the full file path
        file_path = os.path.join(dir_path, filename)

        # Read the Excel file into a pandas dataframe
        df = pd.read_excel(file_path, sheet_name='Ph.D Student Details')

        # Get the sum of the 2nd, 3rd, and 5th columns in the 2nd and 3rd rows
        tot_phd_part_grad = df.iloc[6, [1, 2, 3]].astype(float).sum()
        tot_phd_full_grad = df.iloc[5, [1, 2, 3]].astype(float).sum()

        # Add a new row with the tot_phd_part_grad and tot_phd_full_grad values, along with the file's serial number
        sr_no = int(filename.split('.')[0])
        df_output = df_output.append({'Sr_no': sr_no, 'tot_phd_full_grad': tot_phd_full_grad, 'tot_phd_part_grad': tot_phd_part_grad}, ignore_index=True)

# Save the dataframe as an Excel file named "IPR.xlsx"
df_output.to_excel('GPHD.xlsx', index=False)

print("File saved successfully!")
