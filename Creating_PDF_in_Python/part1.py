from fpdf import FPDF

# create FPDF object
# Layout ('P', 'L') - Potrait or landscape
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4 (default), 'AS', 'Letter', 'Legal', (100, 150)) - width, height

pdf = FPDF('P', 'mm', 'Letter')

# Add a page

pdf.add_page()

# specify font (times, courier, helvetica, symbol, zpfdingbats
# 'B' (Bold), 'U' (underline), 'I' (italics), '' (regular), combination ('BU')
# font size
pdf.set_font('helvetica', 'BIU', 16)

# Add text

# w = width of the cell
# h = height of the cell

# ln helps inject a line break
pdf.cell(40, 10, 'Hello World', ln=True, border=True)
pdf.cell(80, 10, 'Goodbye World')

pdf.output('pdf_1.pdf')





