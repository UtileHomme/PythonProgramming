from PyPDF2 import PdfFileMerger
from os import path, listdir

# append() - add pdf_2 to end of pdf_1
# merge() - insert pdf_2 at specific location of pdf_1
# merge specific page(s) from one pdf to another

#a. Append
# Step 1: Create PDFFile merge object
pdf_merger = PdfFileMerger()

# Step 2: Append pdfs to mergeer
pdf_merger.append('pdf_1.pdf')
pdf_merger.append('pdf_2.pdf')

# Step 3: Write to file
with open(path.abspath('append_1_2.pdf'), 'wb') as append_pdf:
    pdf_merger.write(append_pdf)

# Appending multiple pdfs
pdf_merger2 = PdfFileMerger()

files = [file for file in listdir('.') if path.isfile(file) and file.endswith('.pdf')]

for file in files:
    pdf_merger2.append(file)

with open(path.abspath('append_all_pdf.pdf'), 'wb') as append_all_pdf:
    pdf_merger2.write(append_all_pdf)

#b. Merge

pdf_merger3 = PdfFileMerger()

pdf_merger3.append('pdf_3.pdf')

# Indicate index position of insert and pdf to insert
pdf_merger3.merge(1, 'pdf_1.pdf')

with open(path.abspath('merged_pdf.pdf'), 'wb') as merge_pdf:
    pdf_merger3.write(merge_pdf)

# Merge a section of pdf instead of entire PDF
pdf_merger4 = PdfFileMerger()

pdf_merger4.append('pdf_2.pdf')
pdf_merger4.merge(1, 'pdf_3.pdf', pages = (2,3))

with open(path.abspath('merged_slice.pdf'), 'wb') as merge_slice:
    pdf_merger4.write(merge_slice)









