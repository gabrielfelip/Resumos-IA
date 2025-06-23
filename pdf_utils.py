import PyPDF2
from typing import Union
import io

def extrair_texto_pdf(arquivo: Union[io.BytesIO, any]) -> str:
    texto = ""
    leitor = PyPDF2.PdfReader(arquivo)

    for pagina in leitor.pages:
        texto += pagina.extract_text() or ""

    return texto.strip()