#https://pdfminersix.readthedocs.io/en/latest/

# pip install pdfminer.six
# pdf2txt.py -o output.txt ./testdfg8m6r6.pdf

import pdfminer

from pdfminer.high_level import extract_text
text = extract_text( './testdfg8m6r6.pdf' )
print(repr(text))
'Hello \n\nWorld\n\nHello \n\nWorld\n\nH e l l o  \n\nW o r l d\n\nH e l l o  \n\nW o r l d\n\n\x0c'
print(text)
