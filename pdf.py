import PyPDF2
from PyPDF2 import PdfWriter
import re

path="D:\Dev\Documents\ReleveJuillet2023.pdf"

class Upload:

    def Reade () -> str:

        reader = PyPDF2.PdfReader(input("Taper l'emplacement du pdf"))
        NbrPages = len(reader.pages)
        for i in range(NbrPages-1):
            page = reader.pages[i]
            page_content = page.extract_text()        
        return page_content


reader = PyPDF2.PdfReader(input("Taper l'emplacement du pdf"))
NbrPages = len(reader.pages)
merger = PdfWriter()
print(merger.append(fileobj=reader, pages=(0, NbrPages-1)))
#for i in range(NbrPages-1):
 #   page = reader.pages[i]
  #  page_content = page.extract_text()
 #   print(page_content)
#print(page_content)
#reader = PyPDF2.PdfReader(input("Taper l'emplacement du pdf"))
#NbrPages = len(reader.pages)
#writer.append
#print(page)
#print(Upload.Reade().extract_text())