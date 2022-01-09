#!python3

import os
from PyPDF2 import PdfFileReader
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.pdfpage import PDFPage
from io import BytesIO 
from pdfminer.high_level import extract_text
import re
import numpy as np
import pandas as pd

def extract_info(pdffilepath):
    print("~~~~~~~~~~~~~~~~~This is the Extract Information Function~~~~~~~~~~~~~~~~~")
    with open(pdffilepath, "rb") as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        FileName = os.path.basename(pdffilepath)

        txt = f"""
        information about {FileName}:

        Author: {information.author}
        Creator: {information.creator}
        Producer: {information.producer}
        Subject: {information.subject}k
        Title: {information.title}
        Number of Pages: {number_of_pages}
        """

        print(txt)
        return information


def Extract_PDF_Text(pdffilepath):
    text = extract_text(pdffilepath)
    (Format_PDF(text))
    return text

# Will Split the text extracted from the PDF into Lines
def Format_PDF(PdfText):
    lines = PdfText.split("\n")
    nonEmpty = [line for line in lines if line.strip() != ""]

    formattedtext = ""
    for line in nonEmpty:
        formattedtext += line + "\n"

def Mine_PDF_String(pdffiletext):
    if "Matthew" in pdffiletext:
        print("This text contains Matthew!")
    else:
        print("Not Found")


def main():
        path = r"C:\Users\Matthew\Documents\Personal Documents\Business\Financials\Invoices\6-Komplett-INVOICE NO-KBVF20015557\6-Komplett-INVOICE NO-KBVF20015557.pdf"
        print("path is: " + (path))
        extract_info(path)
        print (Extract_PDF_Text(path))
        Mine_PDF_String(Extract_PDF_Text(path))

        
        
if __name__ == "__main__":
    main()
            