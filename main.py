from PyPDF2 import PdfReader

#! PDF Extractor 
def PDF_data_extractor():
    reader = PdfReader("sample_pdf.pdf")
    for page in reader.pages:
        with open("output_pdf.txt","a", encoding="utf-8") as f:
            f.write(page.extract_text())
    print("PDF has been written in 'output_pdf.txt'.✅")

#! Text Extractor
def text_data_extractor():
    with open("sample_text.txt", "r", encoding="utf-8") as f:
        data = f.read()
        with open("output_text.txt","a", encoding="utf-8") as f:
            f.write(data)
    print("Text has been written in 'output_text.txt'.✅")

if __name__ == "__main__":
    PDF_data_extractor()
    text_data_extractor()