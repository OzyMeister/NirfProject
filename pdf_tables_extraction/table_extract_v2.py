from pdf2docx import Converter
import os
import mammoth
from bs4 import BeautifulSoup
import pandas as pd
import numpy

# # # dir_path for input reading and output files & a for loop # # #
def conv_df_to_csv(tables):
    column_items=[]
    firstcol=[]
    columns1=[]
    columns_data=[]
    df=pd.concat(tables)
    firstcol=df[0].tolist()
    columns1.append(df[0].tolist()[0])
 
    # Select column contents by column  
    # name using [] operator

    columns_data.append(df[0].tolist())
    for i in df.columns:
        if (i%2!=0):
            columns_data.append(df[i].tolist())
        elif (i%2==0 and i!=0):
            columns1.append(df[i].tolist()[0])
        
    transp_data=numpy.transpose(columns_data)
    print(transp_data[1:len(df)])
    print(columns1)
    
    return columns1,transp_data[1:len(df)],firstcol


path_input = 'C:/pdf_tables_extraction/PDFs/'
path_output = 'C:/pdf_tables_extraction/con_docx_files/'
path_output_csv = 'C:/pdf_tables_extraction/csv_files/'

for file in os.listdir(path_input):
    cv = Converter(path_input+file)
    cv.convert(path_output+file+'.docx', start=0, end=2)
    cv.close()
    print(file)


    with open(path_output+file+'.docx', "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        text = result.value
    
    
    soup = BeautifulSoup(result.value, "html.parser")
    soup_str=str(soup)
    #print(soup_str)
    pos1 =soup_str.find('<p><strong>Sanctioned (Approved) Intake</strong></p>')
    pos2=soup_str.find('Total Actual Student Strength (Program(s) Offered by Your Institution)')
    table1str=soup_str[pos1:pos2]
   
    pos3= soup_str.find('<p><strong>Placement &amp; Higher Studies</strong></p>')
    pos4=soup_str.find('<p><strong>Ph.D Student Details')
    table_soup=BeautifulSoup(table1str, "html.parser")
    table_soup1=BeautifulSoup(soup_str[pos3:pos4], "html.parser")
    
    tables = pd.read_html(table_soup.prettify())
    tables2 = pd.read_html(table_soup1.prettify())
    print(tables2)
    
    data1=[]
    columns1=[]
    firstcol1=[]
    df_list=[]
  
    columns1,data1,firstcol1=conv_df_to_csv(tables)
    df1 = pd.DataFrame(data1, columns=columns1)
    df_list.append(df1)
    #df1.to_csv(path_output_csv+file+'.csv', index=(False))
    cnt=2

   
    tb=table_soup1.find_all("table")
    for t in tb:
        data2=[]
        columns2=[]
        firstcol2=[]
        var="df"+str(cnt)
        var=pd.read_html(t.prettify())
        var=pd.concat(var)
        print(var)
        # columns2,data2,firstcol2=conv_df_to_csv(t2)
        
        
       
        # print(data2)
        # var = pd.DataFrame(data2, columns=columns2)
        df_list.append(var)
        cnt=cnt+1
    
    print(df_list)
    for d in df_list:
        print(d)
        d.to_csv(path_output_csv+file+'.csv', index=(False), mode='a')
            
           






    #df.to_csv(path_output_csv+file+'.csv',index=False)
   