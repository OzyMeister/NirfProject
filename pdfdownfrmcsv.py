import csv
import urllib.request
import os

# path to CSV file
csv_file_path = 'NirfDataDown.csv'

# create the directory if it doesn't exist
if not os.path.exists('22pdfs'):
    os.makedirs('22pdfs')

# open CSV file and loop over rows
with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # skip header row
    for row in csv_reader:
        # get link from second column
        link = row[1]
        # get filename from link
        filename = os.path.basename(link)
        # get name from first column
        name = row[0]
        # create new filename with name and extension
        new_filename = name + '_nirf22.pdf'
        # download file and save with new filename
        urllib.request.urlretrieve(link, os.path.join('22pdfs', new_filename))