# Extraer informacion del PDF de Ferroscan enviados por PROFIS Detection

from  PyPDF2 import PdfFileReader

def extraer_informacion (pdf_path):
    with open(pdf_path,  'rb') as f:
        pdf = PdfFileReader(f)
        num_pages = pdf.numPages
        information = pdf.getDocumentInfo()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information

if __name__ == '__main__':
    path = 'reportlab-sample.pdf'
    extraer_informacion(path)