from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Times", "B", 32)
        self.set_xy(0, 40)
        self.cell(0, None, self.title, border=0, new_x="LMARGIN", new_y="NEXT", align="C")
        # The position of the image needs to be calculated by considering the margin and the width of the file.
        self.image("shirtificate.png", x=5, y=70, h=0.75*self.eph, w=200)

    def print_text(self, s):
        self.add_page()
        self.set_margin(0)
        self.set_auto_page_break(auto=False)
        self.set_xy(0, 150)
        self.set_font("Times", size=24)
        self.set_text_color(255, 255,255)
        self.cell(0, None, s, border=0, align="C")


def main():
    pdf = PDF(orientation="Portrait", format="A4")
    pdf.set_title("CS50 Shirtificate")
    pdf.print_text(f"{input('Name: ')} took CS50")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

