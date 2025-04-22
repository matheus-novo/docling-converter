from docling.document_converter import DocumentConverter
import pdfminer.high_level

def pdf_to_md(pdf_path, md_path):
    print("Iniciando Conversão")
    converter = DocumentConverter()
    result = converter.convert(pdf_path)
    print("Result pronto")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(result.document.export_to_markdown())
    print("Escrita realizada")


# Exemplo de uso
pdf_to_md("filosofia.pdf", "filosofia.md")
