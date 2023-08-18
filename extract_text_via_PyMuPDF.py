# you need to install PyMuPDF via pip
# pip install PyMuPDF

import textwrap

import fitz  # PyMuPDF


def process_linebreaks(text):
    # Split by double linebreaks
    chunks = text.split('\n\n')
    
    # Replace single linebreaks in each chunk
    chunks = [chunk.replace('\n', ' ') for chunk in chunks]
    
    # Join chunks with a single linebreak
    return '\n'.join(chunks)



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


# elimnate single line-breaks but keep double line-breaks

text = process_linebreaks(text)

text = textwrap.fill(text, width=80, break_long_words=False, break_on_hyphens=False, expand_tabs=False, drop_whitespace=False, replace_whitespace=False)
print( 'textwrap..........' )
print(text)

# Close the PDF
pdf_document.close()
