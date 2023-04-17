from bs4 import BeautifulSoup
import pandas as pd
import aspose.words as aw
import os
import PyPDF2
import tabula
license = aw.License()
license.set_license("Aspose.Words.Python.NET.lic")
# Open the PDF file
#for m in os.listdir('C:\\Users\\Chetana\\Documents\\Major_Project\\NirfProject-main\\pdf_tables_extraction\\PDFs'):
    # Create a PDF reader object
    
#pdf_file = open('C:\\Users\\Chetana\\Documents\\Major_Project\\NirfProject-main\\pdf_tables_extraction\\PDFs', 'rb')
# Set the path to the directory containing the PDF files
pdf_dir = 'C:\\Users\\Chetana\\Documents\\Major_Project\\NirfProject-main\\pdf_tables_extraction\\PDFs'

# Get a list of PDF files in the directory
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
#print(pdf_files)
# pdf_reader = PyPDF2.PdfReader(pdf_file)
for pdf_file in pdf_files:
    doc = aw.Document(pdf_dir + "\\" + pdf_file)
    doc.save(str(pdf_file).removesuffix(".pdf") + ".html"
             , aw.SaveFormat.HTML)

    # Use Web Scraping to extract tables and text before converting to PDF
    # Path: Output.html

    # Import libraries

    # Read HTML file
    with open(str(pdf_file).removesuffix(".pdf")+".html", "r") as f:
        html = f.read()


    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Extract tables
    tables = soup.find_all("table")

    # Each Table in new Sheet with sheet name = text in <p> before table
    # Create a writer object for the output Excel file
    writer = pd.ExcelWriter("output_" + str(pdf_file) + ".xlsx", engine='xlsxwriter')
    workbook = writer.book

    # Create a list to store the dataframes
    array_tab = []
    df = pd.DataFrame()
    # Loop through the list of dataframes and write each one to a different worksheet
    for i, table in enumerate(tables):
        (max_row, max_col) = df.shape
        # Read the table into a dataframe
        df = pd.read_html(str(table))[0]
        # Get the text in <p> before the table
        # Get the text in <p> before the table
        p_text = table.find_previous_sibling("p").text.replace("*", "").replace(":", "").replace("/",
                                                                                               "").replace("\\", "").replace("?", "").replace("[", "").replace("]", "_")[:30]
        if p_text in workbook.sheetnames:
            df.to_excel(writer, sheet_name=p_text[:30], index=False,
                        header=False, startrow=max_row)
        else:
            df.to_excel(writer, sheet_name=p_text[:30],
                        header=False,
                        index=False)

    # Close the writer object
    #workbook.save("output_" + str(pdf_file) + ".xlsx")
    writer.close()

