from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF(orientation="P", unit="mm", format="A4")
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 30)
        self._pdf.cell(0, 40, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font("helvetica", size=25)
        self._pdf.set_text_color(r=255, g=255, b=255)
        self._pdf.text(60.3, 120, text=f"{name} took CS50")
        self._pdf.output("shirtificate.pdf")

name = input("Name: ")
pdf = PDF(name)