import os
import pandas as pd

# Define the directory containing the Excel files
dir_path = 'Final_Extracted_Excels/'

# Create an empty dataframe to store the results
df_output = pd.DataFrame(columns=['Sr_no', 'faculty_masters'])

# Loop through each file in the directory
for filename in sorted(os.listdir(dir_path)):
    if filename.endswith('.xlsx'):
        # Construct the full file path
        file_path = os.path.join(dir_path, filename)

        try:
            # Read the Excel file into a pandas dataframe
            
            df2 = pd.read_excel(file_path, sheet_name='Faculty Details')

            

            

            faculty_masters = 0

            try:
                for value in df2.iloc[:, 5]:
                    if str(value).lower().startswith(('m', 'p')):
                        faculty_masters += 1  # increment the counter if the condition is true
            except IndexError:
                print(f"Skipping file {filename}: Index out of bounds in accessing column 4 of the dataframe.")
                continue

            sr_no = int(filename.split('.')[0])
            df_output = df_output.append({'Sr_no': sr_no, 'faculty_masters': faculty_masters}, ignore_index=True)

        except ValueError:
            print(f"Skipping file {filename}: Worksheet named 'Sanctioned (Approved) Intake' not found.")

# Save the dataframe as an Excel file named "WD.xlsx"
df_output.to_excel('FSR.xlsx', index=False)

print("File saved successfully!")