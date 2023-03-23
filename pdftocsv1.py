import fitz
import csv

# Open the PDF file
pdf_file = fitz.open(r"C:\Users\Astik\Downloads\IR-E-C-1269.pdf")

# Extract the text from each page of the PDF
texts = []
for page_num in range(pdf_file.page_count):
    page = pdf_file .load_page(page_num)
    texts.append(page.get_text("text"))

# Write the text to a CSV file
with open('1269all.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for text in texts:
        writer.writerow([text])

# Close the PDF file
pdf_file.close()