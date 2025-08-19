import pymupdf


def read_pdf_text(file_path):
    doc = pymupdf.open(stream=file_path, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text
