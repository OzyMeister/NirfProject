import os
import pandas as pd

# Path to the folder containing the excel files
folder_path = 'Dataset/'

# Path to the output Excel file
output_file_path = 'PCS.xlsx'

# Get a list of all the excel files in the folder
file_list = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Sort the file list in ascending order
file_list.sort()

# Create empty lists to store the output data
col1_data = []
col2_data = []
col3_data = []

# Iterate over each file and perform the required operations
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    df = pd.read_excel(file_path, sheet_name='PCS Facilities Facilities of p', header=None)
    col_values = df.iloc[:, 1].str.contains('Yes', case=False)
    result = col_values.astype(int)
    col1_data.append(result.iloc[0])
    col2_data.append(result.iloc[1])
    col3_data.append(result.iloc[2])

# Combine the output data into a single dataframe
output_df = pd.DataFrame({'q1_onehot': col1_data, 'q2_onehot': col2_data, 'q3_onehot': col3_data})

# Write the output to a new Excel file
with pd.ExcelWriter(output_file_path) as writer:
    output_df.to_excel(writer, sheet_name='PCS', index=False)
