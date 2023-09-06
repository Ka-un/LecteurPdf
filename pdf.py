import PyPDF2
from PyPDF2 import PdfWriter, PdfFileMerger
import re

path="D:\Dev\Documents\ReleveJuillet2023.pdf"



class PDFFileReader:
    def __init__ (self, _path):
        """_summary_

        Args:
            _path (string): 
        """  
        self.path = _path       
        self.content = self.Read()
        

    def Read (self) -> str:

        reader = PyPDF2.PdfReader(self.path)
        NbrPages = len(reader.pages)
        content = ""
        for i in range(NbrPages-1):
            page = reader.pages[i]
            content = content + page.extract_text() + "\n"
        return content.splitlines()
    
    def ProcessToDict (self):
        PDFData = {
            "date" : self.ProcessDate(),
            "virements" : []
        }

        DateVirement = r"\d{2}\/\d{2}[A-Z]"
        for i in range(len(self.content)):
            if re.search(DateVirement, self.content[i])!=None:
                print(self.content[i])
                print(self.content[i+1])                
        return PDFData
    
    def ProcessDate (self):
        Date = self.content[2]
        regex = r"\d{2}\s\D{3,9}\d{4}"
        return re.search(regex, Date).group()


process = PDFFileReader(path)
process.ProcessToDict()
#print(process.content)


