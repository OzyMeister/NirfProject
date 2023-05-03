import os
import pandas as pd

# Define the directory containing the Excel files
dir_path = 'Extracted Excels/'

# Create an empty dataframe to store the results
df_output = pd.DataFrame(columns=['Sr_no', 'female_students','total_faculty'])

# Loop through each file in the directory
for filename in sorted(os.listdir(dir_path)):
    if filename.endswith('.xlsx'):
        # Construct the full file path
        file_path = os.path.join(dir_path, filename)

        try:
            # Read the Excel file into a pandas dataframe
            df = pd.read_excel(file_path, sheet_name='Total Actual Student Strength ')
            df2 = pd.read_excel(file_path, sheet_name='Faculty Details')
            # total_outstate = df.iloc[:, 1].replace('-', 0).astype(float).sum()
            # total_sanc_intake_y2 = df.iloc[:, 2].replace('-', 0).astype(float).sum()
            # total_sanc_intake_y3 = df.iloc[:, 3].replace('-', 0).astype(float).sum()
            # female_count = (df2['Gender'] == 'Female').sum()
            female_students = df.iloc[:, 2].replace('-', 0).astype(float).sum()
            # female_faculty = df2.iloc[:, 4].replace('-', 0).female_count
            # female_faculty = (df2.iloc[:, 4] == 'Female').shape[0]
            #female_faculty = df2[df2.Gender == 'Female'].shape[0]
            #female_faculty = df2.Gender.value_counts().Female
            #total_faculty = df2.iloc[:, 0].replace('-', 0).count()
            total_faculty = df2.shape[0]
            # Add a new row with the patent_grant and patent_published values, along with the file's serial number
            sr_no = int(filename.split('.')[0])
            df_output = df_output.append({'Sr_no': sr_no, 'female_students': female_students, 'total_faculty':total_faculty}, ignore_index=True)

        except ValueError:
            print(f"Skipping file {filename}: Worksheet named 'Sanctioned (Approved) Intake' not found.")

# Save the dataframe as an Excel file named "IPR.xlsx"
df_output.to_excel('WD.xlsx', index=False)

print("File saved successfully!")