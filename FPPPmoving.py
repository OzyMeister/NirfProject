import os
import pandas as pd

# Define the directory containing the Excel files
dir_path = 'Dataset/'

# Create an empty dataframe to store the results
df_output = pd.DataFrame(columns=['Sr_no', 'avg_research_fund', 'avg_consult_fund'])

# Loop through each file in the directory
for filename in sorted(os.listdir(dir_path)):
    if filename.endswith('.xlsx'):
        # Construct the full file path
        file_path = os.path.join(dir_path, filename)

        # Read the Excel file into a pandas dataframe
        df1 = pd.read_excel(file_path, sheet_name='Sponsored Research Details')
        df2 = pd.read_excel(file_path, sheet_name='Consultancy Project Details')

        # Convert the relevant columns to numeric data types
        cols_to_sum = [1, 2, 3]
        df1.iloc[2, cols_to_sum] = pd.to_numeric(df1.iloc[2, cols_to_sum])
        df2.iloc[2, cols_to_sum] = pd.to_numeric(df2.iloc[2, cols_to_sum])

        # Get the sum of the 2nd, 3rd, and 5th columns in the 2nd and 3rd rows
        avg_research_fund = df1.iloc[2, cols_to_sum].sum()
        avg_consult_fund = df2.iloc[2, cols_to_sum].sum()

        # Add a new row with the patent_grant and patent_published values, along with the file's serial number
        sr_no = int(filename.split('.')[0])
        df_output = df_output.append({'Sr_no': sr_no, 'avg_research_fund': avg_research_fund, 'avg_consult_fund': avg_consult_fund}, ignore_index=True)

# Save the dataframe as an Excel file named "FPPP.xlsx"
df_output.to_excel('FPPP.xlsx', index=False)

print("File saved successfully!")
