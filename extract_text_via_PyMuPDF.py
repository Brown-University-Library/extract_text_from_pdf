"""
Extracts text from a PDF using PyMuPDF.
Notes...
- A "span" appears to be a word.
- A "block" appears to be a line.
- There is no other indicator of a 'section' other than the notion of a page.
- This means that there is no way to add a line-break between sections.
- To see the text-dict structure, uncomment the "print( 'page_dicts..." line.
"""

import pprint, textwrap
import fitz  # PyMuPDF


FILEPATH = './testdfg8m6r6.pdf'


## open PDF & extract page text-dict --------------------------------
page_dicts = []
with fitz.open( FILEPATH ) as pdf_document:  # type: ignore
    assert type( pdf_document ) == fitz.fitz.Document
    ## loop through pages and extract text-dict data ----------------
    for page_num in range( pdf_document.page_count ):
        assert type( page_num ) == int
        page = pdf_document.load_page( page_num )
        assert type( page ) == fitz.Page
        text_dict = page.get_text( 'dict', flags=fitz.TEXTFLAGS_BLOCKS )  # type: ignore
        page_dicts.append( text_dict )

import json
jsn = json.dumps( page_dicts, sort_keys=True, indent=2 )
with open( './page_dicts.json', 'w' ) as f:
    f.write( jsn )

# print( 'page_dicts, ```%s```' % pprint.pformat(page_dicts) )


## organize the text ------------------------------------------------
all_text = ''
for ( i, page_dict ) in enumerate( page_dicts ):
    # if i > 1:
    #     break
    all_text += f'\n---\nExtracted text for page: {i+1} of {len(page_dicts)}.\n---\n'  # start-page indicator
    blocks = page_dict['blocks']
    for block in blocks:
        block_text = ''
        for ln in block['lines']:
            span_text = ''
            for span in ln['spans']:
                span_text += ' ' + span['text']
                span_text = span_text.replace( '  ', ' ' )
                span_text = span_text.strip()
            block_text += ' ' + span_text
            block_text = block_text.replace( '  ', ' ' )   
            block_text = block_text.strip() 
        # print( f'block_text: ``{block_text}``' )
        # print( '--- endblock ---' )
        # print( ' ' )
        all_text += block_text + '\n'
    
print( 'all_text, ```%s```' % all_text )


## old code below ---------------------------------------------------

## adding textwrap --------------------------------------------------

## elimnate single line-breaks but keep double line-breaks

# text = process_linebreaks(text)

# text = textwrap.fill(text, width=80, break_long_words=False, break_on_hyphens=False, expand_tabs=False, drop_whitespace=False, replace_whitespace=False)
# print( 'textwrap..........' )
# print(text)

## Close the PDF
# pdf_document.close()


## no longer used ---------------------------------------------------
# def process_linebreaks(text):
#     ## Split by double linebreaks
#     chunks = text.split('\n\n')
#     ## Replace single linebreaks in each chunk
#     chunks = [chunk.replace('\n', ' ') for chunk in chunks]
#     ## Join chunks with a single linebreak
#     return '\n'.join(chunks)
