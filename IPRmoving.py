import os
import pandas as pd

# Define the directory containing the Excel files
dir_path = 'Dataset/'

# Create an empty dataframe to store the results
df_output = pd.DataFrame(columns=['Sr_no', 'patent_published', 'patent_grant'])

# Loop through each file in the directory
for filename in sorted(os.listdir(dir_path)):
    if filename.endswith('.xlsx'):
        # Construct the full file path
        file_path = os.path.join(dir_path, filename)

        # Read the Excel file into a pandas dataframe
        df = pd.read_excel(file_path, sheet_name='IPR')

        # Get the sum of the 2nd, 3rd, and 5th columns in the 2nd and 3rd rows
        patent_grant = df.iloc[0, [1, 2, 3]].sum()
        patent_published = df.iloc[1, [1, 2, 3]].sum()

        # Add a new row with the patent_grant and patent_published values, along with the file's serial number
        sr_no = int(filename.split('.')[0])
        df_output = df_output.append({'Sr_no': sr_no, 'patent_published': patent_published, 'patent_grant': patent_grant}, ignore_index=True)

# Save the dataframe as an Excel file named "IPR.xlsx"
df_output.to_excel('IPR.xlsx', index=False)

print("File saved successfully!")
