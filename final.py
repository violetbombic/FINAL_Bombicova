import streamlit as st
import PyPDF2
from PyPDF2 import PdfFileReader
import nltk
from nltk import word_tokenize, sent_tokenize
nltk.download('punkt')
import io
from io import StringIO


st.title("Project_Name")
st.write("Please insert a relative path of the PDF file. Note that the PDF file has to be saved in and copied from the same folder in GitHub, /n where  the .py file is. Try for example: CORE_INTENTIONAL_FEATURES_IN_THE_SYNTACT.pdf")

relative_path = st.file_uploader("Please choose a file")
stringio = StringIO(relative_path.getvalue().decode("UTF-8"))
st.write(stringio)

string_data = stringio.read()
st.write(string_data)

# relative_path = st.text_input('Give me a relative path to PDF file (without the quotes): ')

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
 
# st.write(page_content)
    
# OpenPDF(relative_path)

words_tokens = word_tokenize( page_content )

