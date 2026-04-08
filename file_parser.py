import fitz  # PyMuPDF
import docx
import pytesseract
from PIL import Image
import io

def extract_text(filename, content):
    filename = filename.lower()

    if filename.endswith(".pdf"):
        return extract_pdf(content)
    elif filename.endswith(".docx"):
        return extract_docx(content)
    elif filename.endswith(".txt"):
        return content.decode("utf-8")
    elif filename.endswith((".jpg", ".jpeg", ".png")):
        return extract_image(content)
    else:
        return "Unsupported file format"


def extract_pdf(content):
    text = ""
    pdf = fitz.open(stream=content, filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text


def extract_docx(content):
    doc = docx.Document(io.BytesIO(content))
    return "\n".join([para.text for para in doc.paragraphs])


def extract_image(content):
    image = Image.open(io.BytesIO(content))
    return pytesseract.image_to_string(image)