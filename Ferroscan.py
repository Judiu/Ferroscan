# Extraer informacion del PDF de Ferroscan enviados por PROFIS Detection

from  PyPDF2 import PdfReader

def extraer_informacion (pdf_path):
    with open(pdf_path,  'rb') as f:
        pdf = PdfReader(f)
        num_pages = len(PdfReader.pages)
        information = pdf.getDocumentInfo()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {num_pages}
    """

    print(txt)
    return information

if __name__ == '__main__':
    path = 'E:\LPS Ingenieria Estructural\LPS Ingenieria Estructural - Ferroscan\Informes Entrega Final\CANAPRO PH\DatosCompleto.pdf'
    extraer_informacion(path)