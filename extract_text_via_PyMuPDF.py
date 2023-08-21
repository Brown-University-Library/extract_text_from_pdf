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



## open the PDF -----------------------------------------------------

# pdf_document = fitz.open( './testdfg8m6r6.pdf' )  # type: ignore

page_dicts = []
filepath = './testdfg8m6r6.pdf'
with fitz.open( filepath ) as pdf_document:  # type: ignore
    assert type( pdf_document ) == fitz.fitz.Document
    ## loop through pages and extract text-dict data ----------------
    for page_num in range( pdf_document.page_count ):
        assert type( page_num ) == int
        page = pdf_document.load_page( page_num )
        assert type( page ) == fitz.Page
        text_dict = page.get_text( 'dict', flags=fitz.TEXTFLAGS_BLOCKS )  # type: ignore
        page_dicts.append( text_dict )

print( 'page_dicts, ```%s```' % pprint.pformat(page_dicts) )


## organize the text ------------------------------------------------

all_text = ''
for ( i, page_dict ) in enumerate( page_dicts ):
    all_text += f'---\nExtracted text for page: {i+1} of {len(page_dicts)}.\n---\n\n'
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

        print( f'block_text: ``{block_text}``' )
        print( '--- endblock ---' )
        print( ' ' )
            
        all_text += block_text + '\n\n'
    
    if i > 1:
        break

print( 'all_text, ```%s```' % all_text )
1/0





## Loop through pages and extract text
## POSSIBLE TODO -- this _does_ keep line-blocks -- we'd have to strip out the newlines within a line.
page_data = []
for page_num in range( pdf_document.page_count ):
    assert type( page_num ) == int
    page = pdf_document.load_page( page_num )
    assert type( page ) == fitz.Page
    # foo = page.get_textpage()
    text_dict = page.get_text( 'dict', flags=fitz.TEXTFLAGS_BLOCKS, encoding='utf8' )  # type: ignore
    assert type( text_dict ) == dict, type( text_dict )
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
            span_text += ' ' + span['text']
            span_text = span_text.replace( '  ', ' ' )
            span_text = span_text.strip()
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
