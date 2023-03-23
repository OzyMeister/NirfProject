import tabula
import pandas as pd

# Set the path to your PDF file
pdf_path = r'C:\Users\Astik\Downloads\IR-E-C-1269.pdf'

# Use tabula to extract tables from the PDF file
tables = tabula.read_pdf(pdf_path, pages="all")

# Convert each table into a Pandas DataFrame
dfs = []
for table in tables:
    df = pd.DataFrame(table)
    dfs.append(df)

# Display the resulting DataFrames
for i, df in enumerate(dfs):
    print(f"Table {i+1}")
    print(df)
    print()
