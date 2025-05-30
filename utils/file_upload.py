# utils/file_upload.py

import os
import fitz  # PyMuPDF for PDFs
import docx2txt

def extract_text_from_file(file):
    """
    Extract text from uploaded file based on extension.
    Supports PDF, DOCX, and TXT.
    """
    ext = os.path.splitext(file.name)[-1].lower()
    content = ""

    if ext == ".pdf":
        pdf = fitz.open(stream=file.read(), filetype="pdf")
        for page in pdf:
            content += page.get_text()

    elif ext == ".docx":
        with open("temp.docx", "wb") as f:
            f.write(file.read())
        content = docx2txt.process("temp.docx")
        os.remove("temp.docx")

    elif ext == ".txt":
        content = file.read().decode("utf-8")

    return content

def chunk_text(text, max_tokens=500):
    """
    Simple chunking function that splits text by paragraphs.
    """
    paragraphs = [p.strip() for p in text.split("\n") if len(p.strip()) > 0]
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk.split()) + len(para.split()) < max_tokens:
            current_chunk += "\n" + para
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks
