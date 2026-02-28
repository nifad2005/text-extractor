from PyPDF2 import PdfReader

#! PDF Extractor 
def PDF_data_extractor():
    reader = PdfReader("book.pdf")
    for page in reader.pages:
        with open("pdf_output.txt","a", encoding="utf-8") as f:
            f.write(page.extract_text())
    print("PDF has been written in 'pdf_output.txt'.✅")

#! Text Extractor
def text_data_extractor():
    with open("sample_data.txt", "r", encoding="utf-8") as f:
        data = f.read()
        with open("txt_output.txt","a", encoding="utf-8") as f:
            f.write(data)
    print("Text has been written in 'txt_output.txt'.✅")

if __name__ == "__main__":
    PDF_data_extractor()
    text_data_extractor()