import streamlit as st
import PyPDF2
from PyPDF2 import PdfFileReader

relative_path = st.text_input('Give me a relative path to PDF file (without the quotes): ')

# def OpenPDF(relative_path):

  

# creating a pdf file object 
objfile = open(relative_path, 'rb') 

# creating a pdf reader object 
pdfReader = PdfFileReader(objfile) 

# printing number of pages in pdf file 
num_pages = pdfReader.numPages

# creating a page object 
pageObj = pdfReader.getPage(1) 

# extracting text from page 
text = pageObj.extract_text


# closing the pdf file object 
objfile.close()

page_content=""
with open(relative_path,'rb') as pdf_file:
  read_pdf = PyPDF2.PdfFileReader(pdf_file)
  number_of_pages = read_pdf.getNumPages()
  for page_number in range(number_of_pages):
    page = read_pdf.getPage(page_number)
    page_content += page.extract_text()
    
# OpenPDF(relative_path)
