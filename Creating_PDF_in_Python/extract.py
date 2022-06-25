from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
import re

pdf = PdfFileReader('pdf_4.pdf')

page_1_object = pdf.getPage(1)
# print(page_1_object)

# Step 2: Extract Text

page_1_text = page_1_object.extractText()
# print(page_1_text)

# 1. Combined the text from all Pages and save as text file

with Path('pdf_4.txt').open(mode='w') as output_file:
    text = ''
    for page in pdf.pages:
        text = text + page.extractText()

    output_file.write(text)

# How to find a particular string in all pages of PDF
# Page numbers list
search_pages = []

totalpages = pdf.getNumPages()
print(totalpages)
for i in range(0, totalpages):
    # add +1 to page number if you want the actual page numbrer and not the index
    page_1_object = pdf.getPage(i)
    # print(page_1_object)
    page_text = page_1_object.extractText()

    if 'year' in page_text:
        search_pages.append(i)

print(search_pages)

# 2. Adding all the pdfs which have the search string into a new pdf

# Create PDF file reader object

input_pdf = PdfFileReader('pdf_4.pdf')

pdf_writer = PdfFileWriter()

# Get text from pages with search string
for page in search_pages:
    page_object = input_pdf.getPage(page)
    pdf_writer.addPage(page_object)

# Save Pages as PDF

with Path('searched_pages.pdf').open(mode='wb') as output_file_2:
    pdf_writer.write(output_file_2)

# 3. How to get only the sentence in which searched string is

pages_sentences = []
for i in range(0, totalpages):
    # add +1 to page number if you want the actual page numbrer and not the index
    page_1_object = pdf.getPage(i)
    # print(page_1_object)
    page_text = page_1_object.extractText()

    if 'year' in page_text:
        sentence_list = ['page ' + str(i) + ': ' + sentence.replace('\n', '') for sentence in re.split('\. \W+|\?\W+|\!\W+', page_text)
                         if 'year' in sentence][0]
        print(sentence_list)
        pages_sentences.append(sentence_list)

text = '\n'.join(pages_sentences)

with Path('searched_string.txt').open(mode='w') as output_file3:
    output_file3.write(text)


