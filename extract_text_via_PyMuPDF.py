# you need to install PyMuPDF via pip
# pip install PyMuPDF

import fitz  # PyMuPDF

# Open the PDF
pdf_document = fitz.open( './testdfg8m6r6.pdf' )

# Loop through pages and extract text
for page_num in range(pdf_document.page_count):
    page = pdf_document.load_page(page_num)
    text = page.get_text("text")
    print(text)

# Close the PDF
pdf_document.close()
