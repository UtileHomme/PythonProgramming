from fpdf import FPDF

title = '20,000 leagues under the Sea'


class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 15)

        # Calculate width of title and position
        title_width = self.get_string_width(title) + 6

        # PDF width
        doc_w = self.w
        self.set_x((doc_w - title_width) / 2)

        # Colors of the frame, background and text

        self.set_draw_color(0, 80, 180)  # border = blue

        self.set_fill_color(230, 230, 0)  # background = yellow

        self.set_text_color(220, 50, 50)  # text = red

        # Thickness of frame(border)

        self.set_line_width(1)

        # Title
        self.cell(title_width, 10, title, border=1, ln=1, align='C', fill=1)
        # Line break
        self.ln(10)

    def footer(self):
        # Set position of footer
        self.set_y(-15)

        # Set font
        self.set_font('helvetica', 'I', 8)

        # Set font color grey
        self.set_text_color(169, 169, 169)

        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

    # Adding chapter title to start of each chapter
    def chapter_title(self, ch_num, ch_title):
        self.set_font('helvetica', '', 12)

        self.set_fill_color(200, 220, 255)

        chapter_title = f'Chapter {ch_num} : {ch_title}'

        self.cell(0, 5, chapter_title, ln=1, fill=1)

    # Chapter content
    def chapter_body(self, name):
        # Read text file

        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')

        # set font
        self.set_font('times', '', 12)

        # insert text
        self.multi_cell(0, 5, txt)

        # line break
        self.ln()

        # End of chapter
        self.set_font('times', 'I', 12)

        self.cell(0, 5, 'End of Chapter')

    def print_chapter(self, ch_num, ch_title, name):
        self.add_page()
        self.chapter_title(ch_num, ch_title)
        self.chapter_body(name)

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

pdf.print_chapter(1, 'A Runaway Reef', 'chp1.txt')
pdf.print_chapter(2, 'The Pros and Cons', 'chp2.txt')

pdf.output('pdf_3.pdf')
