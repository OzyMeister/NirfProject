import re
import csv

# Open the original CSV file
with open('1269all.csv', 'r') as f:

    # Read the contents of the file
    contents = f.read()

    # Use regex to extract the years from the first row
    pattern = r'Academic Year([\s\S]*?)UG'
    years_match = re.search(pattern, contents)
    years = years_match.group(1).strip().split('\n')

    # Use regex to extract the UG and PG data from the first row
    pattern = r'UG \[4 Years Program\(s\)\]([\s\S]*?)PG \[2 Year Program\(s\)\]'
    data_match = re.search(pattern, contents)
    data = data_match.group(1).strip().split('\n')

    # Write the new data to a CSV file
    with open('xtrc1.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(years)
        writer.writerow(data)