# brief/utils.py

import os
# utils.py
from PyPDF2 import PdfReader, PdfWriter
import io

def edit_pdf(file, text_to_add="Modified"):
    reader = PdfReader(file)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # Add metadata or annotation (or replace content logic)
    writer.add_metadata({"/ModifiedBy": text_to_add})

    buffer = io.BytesIO()
    writer.write(buffer)
    buffer.seek(0)
    return buffer


def generate_brief_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.pdf':
        return "This is a PDF document. Contents: (simulated brief summary)."
    elif ext in '.pptx':
        return "This is a powerpoint presentation. Contents: (simulated brief summary)."
    elif ext in ['.docx', '.doc']:
        return "This is a Word document. Contents: (simulated brief summary)."
    elif ext == '.xlsx':
        return "This is an Excel file. Contents: (simulated brief summary)."
    elif ext == '.csv':
        return "This is a CSV file. Contents: (simulated brief summary)."
    else:
        return "Unsupported file format for summarization."