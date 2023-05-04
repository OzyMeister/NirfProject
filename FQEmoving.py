import os
import pandas as pd

# Define the directory containing the Excel files
dir_path = 'Final_Extracted_Excels/'

# Create an empty dataframe to store the results
df_output = pd.DataFrame(columns=['Sr_no', 'f1_exp_count', 'f3_exp_count', 'f2_exp_count'])

# Loop through each file in the directory
for filename in sorted(os.listdir(dir_path)):
    if filename.endswith('.xlsx'):
        # Construct the full file path
        file_path = os.path.join(dir_path, filename)

        try:
            # Read the Excel file into a pandas dataframe
            
            df2 = pd.read_excel(file_path, sheet_name='Faculty Details')

            # Count the number of rows that meet each condition using value_counts function
            f1_exp_count = len(df2.loc[df2.iloc[:,6] <= 96])
            f2_exp_count = len(df2.loc[(df2.iloc[:,6] > 96) & (df2.iloc[:,6] <= 180)])
            f3_exp_count = len(df2.loc[df2.iloc[:,6] > 180])

            sr_no = int(filename.split('.')[0])
            df_output = df_output.append({'Sr_no': sr_no, 'f1_exp_count': f1_exp_count, 'f2_exp_count': f2_exp_count, 'f3_exp_count': f3_exp_count}, ignore_index=True)

        except IndexError:
            print(f"Skipping file {filename}: Index out of bounds in accessing column 7 of the dataframe.")
            continue

        except ValueError:
            print(f"Skipping file {filename}: Worksheet named 'Sanctioned (Approved) Intake' not found.")

# Save the dataframe as an Excel file named "FQE.xlsx"
df_output.to_excel('FQE.xlsx', index=False)

print("File saved successfully!")