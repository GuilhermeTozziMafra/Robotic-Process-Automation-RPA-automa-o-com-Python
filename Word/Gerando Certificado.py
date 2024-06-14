from docx import Document
from docx.shared import Pt

arquivoWord = Document("C:\Users\guilherme.mafra\Desktop\Python\Word\Certificado1.docx")

#Seleciona o estilo
estilo = arquivoWord.styles["Normal"]

for paragrafo in arquivoWord.paragraphs:

    if "@nome" in paragrafo.text:
        paragrafo.text = "Berenice Rosa Santos"

#Salvando o certificado do aluno
arquivoWord.save("Berenice Rosa Santos.docx")