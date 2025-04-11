# utils/pdf_reader.py
from pdf2image import convert_from_path
import pytesseract
import fitz  # PyMuPDF

def extract_text_from_pdf(file_path: str) -> str:
    try:
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        if text.strip():
            return text
        else:
            return extract_text_with_ocr(file_path)
    except Exception as e:
        return f"Error reading PDF: {e}"

def extract_text_with_ocr(file_path: str) -> str:
    images = convert_from_path(file_path)
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)
    return text
