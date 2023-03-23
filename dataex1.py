import csv
import re

input_file = '1269all.csv'  # Replace with the name of your input CSV file
output_file = 'xtrc1.csv'  # Replace with the name of your output CSV file

# Define a regular expression pattern to match the academic years in the first row
pattern = r'Academic\s+Year\s+(\d{4}-\d{2})\s*(\d{4}-\d{2})\s*(\d{4}-\d{2})\s*(\d{4}-\d{2})\s*(\d{4}-\d{2})\s*(\d{4}-\d{2})'

with open(input_file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)  # Read the first row as the header
    header = [col.replace('\n', '') for col in header]  # Remove newline characters from header
    match = re.search(pattern, ' '.join(header))  # Combine header cells into a string and search for the pattern
    if match:
        years = [match.group(i) for i in range(1, 7)]
        # Extract the years from the capturing groups and store them in a list
        output_writer = csv.writer(open(output_file, 'w', newline=''))
        # Create a CSV writer for the output file
        output_writer.writerow(years)  # Write the years as the header row in the output file
        for row in reader:
            year_values = []
            for year in years:
                year_header = f'{year}-UG'
                if year_header in header:
                    year_index = header.index(year_header)
                else:
                    year_index = header.index(year.strip())
                year_values.append(row[year_index])
            output_writer.writerow(year_values)
            # Write the cell values for each year as a row in the output file