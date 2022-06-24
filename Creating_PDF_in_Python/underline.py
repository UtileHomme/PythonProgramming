from fpdf import FPDF

from PIL import ImageFont


def get_text_width(text_string, font):
    return font.getmask(text_string).getbbox()[2] / 2.6


# create FPDF object
# Layout ('P', 'L') - Potrait or landscape
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4 (default), 'AS', 'Letter', 'Legal', (100, 150)) - width, height

pdf = FPDF('P', 'mm', 'Letter')

# Add a page

pdf.add_page()

# Add Image font

font = ImageFont.truetype('times.ttf', 12)

pdf.set_font('times', '', 12)

text_string_1 = 'Hello'

pdf.cell(get_text_width(text_string_1, font), 10, text_string_1, ln=False)

pdf.set_font('times', 'u', 12)

text_string_2 = 'world'

pdf.cell(get_text_width(text_string_2, font), 10, text_string_2, ln=False)

pdf.set_font('times', '', 12)

text_string_3 = 'this is me'

pdf.cell(get_text_width(text_string_3, font), 10, text_string_3, ln=False)


# specify font (times, courier, helvetica, symbol, zpfdingbats
# 'B' (Bold), 'U' (underline), 'I' (italics), '' (regular), combination ('BU')
# font size
# pdf.set_font('helvetica', 'BIU', 16)
# pdf.set_font('Blackadder', '', 16)

# Add text

# w = width of the cell
# h = height of the cell

# ln helps inject a line break
# pdf.cell(40, 10, 'Hello World', ln=True, border=True)
# pdf.cell(80, 10, 'Goodbye World')

pdf.output('pdf_5.pdf')
