# RAG System (PDF Reader)

This project is a simple data-ingestion starter for a Retrieval-Augmented Generation (RAG) workflow.

Current functionality:
- Extracts all text from `PDF Reader/book.pdf` into `PDF Reader/pdf_output.txt`
- Copies text from `PDF Reader/sample_data.txt` into `PDF Reader/txt_output.txt`

## Project Structure

```text
    main.py
    book.pdf
    sample_data.txt
    pdf_output.txt
    txt_output.txt
    README.MD
```

## Requirements

- Python 3.8+
- `PyPDF2`

Install dependency:

```bash
pip install PyPDF2
```

## How to Run

From the `PDF Reader` folder:

```bash
python main.py
```

The script runs two functions:
- `PDF_data_extractor()`: reads `book.pdf` and appends extracted text to `pdf_output.txt`
- `text_data_extractor()`: reads `sample_data.txt` and appends text to `txt_output.txt`

## Important Notes

- Output files are opened in append mode (`"a"`), so running the script multiple times duplicates content.
- Paths in `main.py` are relative, so run from inside `PDF Reader` unless you update the paths.
- Some PDFs may produce encoding artifacts when extracted (for example, `Ã©` instead of `é`), depending on source font/encoding.

## Suggested Next Steps

- Clear output files before each run or switch to write mode (`"w"`) when needed.
- Split extracted text into chunks for embedding.
- Add a vector store (FAISS/Chroma) and retrieval layer to complete the RAG pipeline.


---
This README file is written by AI.
---
