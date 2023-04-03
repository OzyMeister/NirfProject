import PyPDF2
import os
import tabula
import pandas as pd
from PyPDF2 import PdfReader
from tabula.io import read_pdf


# Set the path to the directory containing the PDF files
pdf_dir = 'C:\\Users\\Chetana\\Documents\\Major_Project\\NirfProject-main\\pdf_tables_extraction\\PDFs'

# Get a list of PDF files in the directory
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
print(pdf_files)
# Loop through the PDF files and process each one with PyPDF2
for pdf_file in pdf_files:
    #filename = os.path.join(pdf_dir, pdf_file)

    with open(os.path.join(pdf_dir, pdf_file), 'rb') as pdf:
        pdf_reader = PyPDF2.PdfReader (pdf)
        # Process the PDF here
        # For example, you can get the number of pages in the PDF:
        pages = len(pdf_reader.pages)
#print(len(pages))
# Use tabula to extract tables from each page
        all_tables = []
        for page in range(1, pages + 1):
            tables = read_pdf(pdf, pages=page, multiple_tables=True)
            all_tables.extend(tables)

        # Store each table in a separate CSV file
        for i, table in enumerate(all_tables):
            filename = f'table_{pdf_file + str(i+ 1)}.csv'
            table.to_csv(filename, index=False)
                #print(f"{pdf_file} has {pages} pages.")


# Open the PDF file in binary mode
#with open(r'C:\\Users\\Chetana\\Documents\\Major_Project\\NirfProject-main\\pdf_tables_extraction\\PDFs\\Anna University_20220218-NIRF_2022_IR-E-U-0439.pdf', 'rb') as file:
    # Read the PDF content
    #pdf_content = file.read()

# Use PyPDF2 to extract all page numbers
#pdf_reader = PyPDF2.PdfReader(r'C:\\Users\\Chetana\\Documents\\Major_Project\\NirfProject-main\\pdf_tables_extraction\\PDFs\\Anna University_20220218-NIRF_2022_IR-E-U-0439.pdf')

