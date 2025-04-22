from docling.document_converter import DocumentConverter
#from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import pdfminer.high_level


def verificar_convertidos():
    print("Iniciando DEF - verificar_convertidos")
    pasta_MD = './MDs'
    arquivos_MD = []

    pasta_PDF = './PDFs'

    for arquivo in os.listdir(pasta_MD):
        filename = arquivo.split(".", 1)[0]
        if filename != '':
            print("Feito o append do " + filename + ", no arquivos_MD")
            arquivos_MD.append(filename)

    for arquivo in os.listdir(pasta_PDF):
        filename = arquivo.split(".", 1)[0]
        if filename not in arquivos_MD:
            print("Chamar para converter esse " + filename)
            pdf_to_md(filename=filename)



def pdf_to_md(filename):
    md_path = './MDs'
    pdf_path = './PDFs'

    pdf_file = os.path.join(pdf_path, f'{filename}.pdf')
    md_file = os.path.join(md_path, f'{filename}.md')

    print("Iniciando Conversão")
    converter = DocumentConverter()
    result = converter.convert(pdf_file)
    print("Result pronto")
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(result.document.export_to_markdown())
    print("Escrita realizada do: " + pdf_file)



verificar_convertidos()
# Exemplo de uso
#pdf_to_md("PDFs/filosofia.pdf", "filosofia.md")

#text_splitter = RecursiveCharacterTextSplitter(
#    chunk_size=500,  # Tamanho dos chunks
#    chunk_overlap=50  # Sobreposição para contexto
#)
#chunks = text_splitter.split_text(text)


