import fitz


def pdf_to_text(pdf_file):
    text=""
    with fitz.open(stream=pdf_file.read(),filetype="pdf") as doc:
        for page in doc:
            text = text + page.get_text()
    return text.strip()