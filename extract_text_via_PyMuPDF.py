# you need to install PyMuPDF via pip
# pip install PyMuPDF

import fitz  # PyMuPDF

# Open the PDF
pdf_document = fitz.open( './testdfg8m6r6.pdf' )

# Loop through pages and extract text
text = ''
for page_num in range(pdf_document.page_count):
    page = pdf_document.load_page(page_num)
    text = page.get_text("text")
    print( 'raw output..........' )
    print(text)

## adding textwrap............

# wrap text, which has too many line-breaks

import textwrap
# text = textwrap.dedent(text).strip()

# eliminate line-breaks
# text = text.replace('\n', ' ')

#

text = textwrap.fill(text, width=80, break_long_words=False, break_on_hyphens=False, expand_tabs=False, drop_whitespace=False, replace_whitespace=False)
print( 'textwrap..........' )
print(text)

# Close the PDF
pdf_document.close()
