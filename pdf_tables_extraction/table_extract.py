from pdf2docx import Converter
import os
import mammoth
from bs4 import BeautifulSoup
import pandas as pd

# # # dir_path for input reading and output files & a for loop # # #

path_input = 'C:/pdf_tables_extraction/PDFs/'
path_output = 'C:/pdf_tables_extraction/con_docx_files/'
path_output_csv = 'C:/pdf_tables_extraction/csv_files/'

dfs = []

for file in os.listdir(path_input):
    cv = Converter(path_input+file)
    cv.convert(path_output+file+'.docx', start=0, end=3)
    cv.close()
    print(file)


    with open(path_output+file+'.docx', "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        text = result.value
        print(text)
    
    soup = BeautifulSoup(result.value, "html.parser")
    soup_str=str(soup)
    #print(soup_str)
    # pos1 =soup_str.find('<p><strong>Sanctioned (Approved) Intake</strong></p>')
    # pos2=soup_str.find('Total Actual Student Strength (Program(s) Offered by Your Institution)')
    pos1 =soup_str.find('<p><strong>Placement &amp; Higher Studies</strong></p>')
    pos2=soup_str.find('<p><strong>Ph.D Student Details </strong>')
    table1str=soup_str[pos1:pos2]
    # print(table1str)
   
    # table_soup=BeautifulSoup(table1str, "html.parser")
    # print(table_soup.prettify())
    # header = table_soup.find_all("table")[0].find("tr")

  
# for getting the header from
# the HTML file
    # list_header = []
    # for items in header:
    #     try:
    #         list_header.append(items.get_text())
    #     except:
    #         continue
    
    # # for getting the data
    # HTML_data = soup.find_all("table")[0].find_all("tr")[1:]
    
    # for element in HTML_data:
    #     sub_data = []
    #     for sub_element in element:
    #         try:
    #             sub_data.append(sub_element.get_text())
    #         except:
    #             continue
    #     data.append(sub_data)
    
    # Storing the data into Pandas
    # DataFrame
    # tables = pd.read_html(table_soup.prettify())
    # data=[]
    # headers=[]
    # print("tables     ")
    # new=tables[0]
    
    # df=pd.concat(tables)
   
        # for i in range(len(tables)):
    #     for j in range(len(tables[i])):
    #         print(tables[i][j])
    #         #data.append(tables[i][j])
    # #df = pd.DataFrame(data,columns =headers)
    # print(data)
    # print(headers)
    #df = pd.concat(pd.read_html(table_soup.prettify()) for fl in )
    #df.to_csv("H:\\test1.csv", index = False)

    # df.to_csv(path_output_csv+file+'.csv',index=False)
    # df1=pd.read_csv(path_output_csv+file+'.csv')
    # rows = len(df1.axes[0])
    # cols = len(df1.axes[1])
    # data=[]
    # columns=[]
    # print(rows)
    # print(cols)




    #dataFrame = pd.read_html(html)
    
    # Converting Pandas DataFrame
    # into CSV file
    #dataFrame.to_csv(path_output_csv+file+'.csv')




       # Converting the table HTML content to Pandas DataFrame
    df = pd.read_html(table1str)[0]
    
    # Saving the extracted table as a CSV file
    df.to_csv(path_output_csv+file+'.csv',index=False)
    
    # Reading the CSV file and getting its dimensions
    df1=pd.read_csv(path_output_csv+file+'.csv')
    rows = len(df1.axes[0])
    cols = len(df1.axes[1])
    data=[]
    columns=[]
    print(rows)
    print(cols)