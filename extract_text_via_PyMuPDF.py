# you need to install PyMuPDF via pip
# pip install PyMuPDF

import pprint, textwrap

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

## Loop through pages and extract text
# text = ''
# for page_num in range(pdf_document.page_count):
#     page = pdf_document.load_page(page_num)
#     text = page.get_text("text", flags=fitz.TEXTFLAGS_BLOCKS)
#     break
    
# print( 'raw output..........' )
# print(text)


## Loop through pages and extract text
## POSSIBLE TODO -- this _does_ keep line-blocks -- we'd have to strip out the newlines within a line.
text = ''
for page_num in range(pdf_document.page_count):
    page = pdf_document.load_page(page_num)
    # text = page.get_text("xml", flags=fitz.TEXTFLAGS_BLOCKS)
    # text = page.get_text("blocks")
    text = page.get_text("dict", flags=fitz.TEXTFLAGS_BLOCKS)
    break
    
# print( 'raw output..........' )
# pprint.pprint(text)


## analyze ----------------
all_text = ''
blocks = text['blocks']
for block in blocks:
    block_text = ''
    print( '--- block ---' )
    for ln in block['lines']:
        span_text = ''
        for span in ln['spans']:
            # print( '--- span ---' )
            span_text += span['text']
            # print('--- endspan ---')
        # print( f'span_text: ``{span_text}``' )
        block_text += ' ' + span_text
        block_text = block_text.replace( '  ', ' ' )   
        block_text = block_text.strip() 
    print( f'block_text: ``{block_text}``' )
    print( '--- endblock ---' )
    print( ' ' )



# all_text = ''
# blocks = text['blocks']
# for block in blocks:
#     block_text = ''
#     print( '--- block ---' )
#     for ln in block['lines']:
#         for span in ln['spans']:
#             # print( '--- span ---' )
#             # print( span['text'] )
#             print( span['text'].strip(), end=' ' )
#             # print('--- endspan ---')
#     print( '--- endblock ---' )
#     print( ' ' )




## adding textwrap............


# elimnate single line-breaks but keep double line-breaks

# text = process_linebreaks(text)

# text = textwrap.fill(text, width=80, break_long_words=False, break_on_hyphens=False, expand_tabs=False, drop_whitespace=False, replace_whitespace=False)
# print( 'textwrap..........' )
# print(text)

# Close the PDF
pdf_document.close()
