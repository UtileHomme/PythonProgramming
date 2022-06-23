from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Logo
        # x, y coordinates, width and height = 0
        self.image('fox_face.png', 10, 8, 25)
        self.set_font('helvetica', 'B', 20)
        # Padding
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', border=True, ln=True, align='C')
        # Line break
        self.ln(20)

    def footer(self):
        # Set position of footer
        self.set_y(-15)

        # Set font
        self.set_font('helvetica', 'I', 10)

        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')


# create FPDF object
# Layout ('P', 'L') - Potrait or landscape
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4 (default), 'AS', 'Letter', 'Legal', (100, 150)) - width, height

# pdf = FPDF('P', 'mm', 'Letter')
pdf = PDF('P', 'mm', 'Letter')

# To get the total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto=True, margin=15)

# Add a page

pdf.add_page()

# specify font (times, courier, helvetica, symbol, zpfdingbats
# 'B' (Bold), 'U' (underline), 'I' (italics), '' (regular), combination ('BU')
# font size
pdf.set_font('helvetica', '', 12)
# pdf.set_text_color(220,50,50)

# Add text

# w = width of the cell
# h = height of the cell

# ln helps inject a line break
# pdf.cell(40, 10, 'Hello World', ln=True, border=True)
for i in range(1, 41):
    # width of zero means entire line of the PDF
    pdf.cell(0, 10, f'This is line {i} :D', ln=True)

pdf.output('pdf_2.pdf')
