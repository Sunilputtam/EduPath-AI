from pathlib import Path
from pypdf import PdfReader
from docx import Document

def extract_text(uploaded_file):
    name = uploaded_file.name.lower()
    if name.endswith('.pdf'):
        reader = PdfReader(uploaded_file)
        return '\n'.join((p.extract_text() or '') for p in reader.pages)
    if name.endswith('.docx'):
        doc = Document(uploaded_file)
        return '\n'.join(p.text for p in doc.paragraphs)
    if name.endswith('.txt'):
        return uploaded_file.getvalue().decode('utf-8', errors='ignore')
    raise ValueError('Supported formats: PDF, DOCX, TXT')
