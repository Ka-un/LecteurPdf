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

    def Read (self) -> str:

        reader = PyPDF2.PdfReader(self.path)
        NbrPages = len(reader.pages)
        content = ""
        for i in range(NbrPages-1):
            page = reader.pages[i]
            content = content + page.extract_text()        
        return content.splitlines()
    
    def ProcessToDict (self):
        contentProcess = self.Read()
        PDFData = {}
        return contentProcess
    
    def ProcessDate (self):
        contentProcessDate = self.Read()
        Date = contentProcessDate[2]
        regex = '/\d{2}\s\D{3,9}\d{4}/'
        matches = re.finditer(regex, Date)
        print(matches)

        return


process = PDFFileReader(path)
#print(process.ProcessToDict())
process.ProcessDate()

