from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]


for pdf in files:
    merger.append(pdf)

merger.write("mereged-pdf.pdf")
merger.close()

## Sorted pdf in array

from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]


for pdf in["2.pdf","1.pdf","3.pdf"]:
    merger.append(pdf)

merger.write("mereged-pdf.pdf")
merger.close()
