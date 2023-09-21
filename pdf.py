from PyPDF2 import PdfReader
import re
import json

path="D:\Dev\Documents\ReleveSeptembre2023.pdf"



class PDFFileReader:
    def __init__ (self, _path):
        """Constructeur de PDFFileReader, 
        assigne les valeurs par défaut de path et content
f
        Args:
            _path (string): path correspond au chemin du PDF à lire
        """  
        self.path = _path       
        self.content = self.Read()
        

    def Read (self) -> str:
        """Utilise PDF2.PdfReader pour lire le Document PDF 
        et le concatener toutes les pages en un objet

        Returns:
            str: retourne toutes les pages du Document 
            dans une liste de Str séparé à chaque saut de ligne
        """
        reader = PdfReader(self.path)
        NbrPages = len(reader.pages)
        content = ""
        for i in range(NbrPages-1):
            page = reader.pages[i]
            #content est un Str
            content = content + page.extract_text() + "\n"    
        #content en transformé en list par splitlines    
        return content.splitlines()
    
    def ProcessToDict (self):
        """Itére sur toutes les lignes de self.content et extrait les
        informations dans un dictionnaire PDFData et le retourne

        Returns:
            DICT : retourne PDFData = Dictionnaire sous forme 
                PDFdata={

                    date: {year: 2023, month: 07, day: 05},

                    virements:
                        [
                            {
                            account: XXXXXX,

                            entity: Carrefour,

                            date: {year: 2023, month: 07, day: 05},

                            amount: 50.63

                            }
                        ]
                        }
        """
        PDFData = {
            "date" : self.ProcessDate(),
            "virements" : []
        }

        DateVirement = r"\d{2}\/\d{2}[A-Z]"
        Montant = r"\d{2}\,\d{2}"
        EntityCB = r"CB(\s[a-zA-Z]{1,100}){0,10}"
        Date = r"\d{2}\/\d{2}"
        for i in range(len(self.content)-1):
            if re.search(DateVirement, self.content[i])!=None:
                entity1 = re.search(Montant, self.content[i+1])
                entity2 = re.search(EntityCB, self.content[i])
                entity3 = re.search(Date, self.content[i])
                if entity1 != None and entity2 != None:                    
                    PDFData["virements"].append({"montant" : entity1.group(), "entite" : entity2.group()[3:], "moyen" : "CB", "date" : entity3.group()})
                elif entity1 != None:
                    position = re.search(r"\s", self.content[i]).span()
                    PDFData["virements"].append({"montant" : entity1.group(), "entite" : self.content[i][position[0]:], "moyen" : self.content[i][5:position[0]], "date" : entity3.group()})    
        return PDFData
    
    def ProcessDate (self):
        """Cherche la date du document

        Returns:
            _type_: cherche la date du document et la renvoie en Str
        """
        Date = self.content[2]
        regex = r"\d{2}\s\D{3,15}\d{4}"
        return re.search(regex, Date).group()
    
    def ExportToJson (self):
        """
        
        """
        mon_fichier = open("data.json", "w")
        json.dump(self.ProcessToDict(),  mon_fichier, indent = 3)
        mon_fichier.close()
        


process = PDFFileReader(path)
process.DownloadData()
#print(process.content)


