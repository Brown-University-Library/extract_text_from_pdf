# Purpose

To experiment with extracting text from newer Brown Daily Herald PDFs.

Reason: The existing extract_text.py script uses a very old pdf-to-text linux library, that yields poor results.

---

Times...

python ./extract_text_via_PyMuPDF.py  0.08s user 0.02s system 83% cpu 0.123 total

python ./extract_text_via_pdfminer.py  3.49s user 0.08s system 99% cpu 3.603 total

python ./extract_text_via_pypdf2.py  0.13s user 0.04s system 89% cpu 0.187 total

---