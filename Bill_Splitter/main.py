from fpdf import FPDF
import os
import webbrowser

class Bill:
    """
    Class having information about the bill such as bill amount, period of the bill.
    """
    
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Create a Flatmate person with information as name, days they stay, and a method to calculate respective pay.
    """

    def __init__(self, name, days_in_flat):
        self.name = name
        self.days = days_in_flat

    def pays(self, bill, other_flatmate):
        proportion = self.days / (self.days + other_flatmate.days)
        return round(bill.amount * proportion,2)

class PDFReport:
    """
    Class to create PDF report along with necessary information.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        
        # setting up the pdf properties
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.set_font(family="Arial", size= 20, style="BU")
        pdf.add_page()

        # Adding the header
        pdf.cell(w=0, h=50, txt="Bill Splitter", align="C",ln=1)

        # Changing text properties and adding period 
        pdf.set_font(family="Arial", size=8, style= "B")
        pdf.cell(w=0, h=20, txt= bill.period, align="R", ln=1)
        pdf.cell(w=0,h=10,ln=1)

        # Changing text properties again and adding Table heading
        pdf.set_font(family="Arial", size=12, style= "B")
        pdf.cell(w=230, h=30, txt="Flatmate", align="C", border=1)
        pdf.cell(w=150, h=30, txt="Period", align="C",border=1)
        pdf.cell(w=150, h=30, txt="Payment", align="C",border=1,ln=1)
        
        # Adding content 
        pdf.set_font(family="Arial", size=10)
        pdf.cell(w=0, h=10, ln=1)
        pdf.cell(w=230, h=20, txt=mate1.name, align="C")
        pdf.cell(w=150, h=20, txt=str(mate1.days), align="C")
        pdf.cell(w=150, h=20, txt=str(mate1.pays(bill,mate2)), align="C",ln=1)
        pdf.cell(w=230, h=20, txt=mate2.name, align="C")
        pdf.cell(w=150, h=20, txt=str(mate2.days), align="C")
        pdf.cell(w=150, h=20, txt=str(mate2.pays(bill,mate1)), align="C",ln=1)

        os.chdir('./Bill_Splitter/reports')
        pdf.output(self.filename)

        #To open pdf file automatically (only locally)
        webbrowser.open(self.filename)         

bill = Bill(float(input("Enter Bill Amount: ")), input("Enter the Bill Period [Ex. January 2022]: "))

mate1 = Flatmate(input("1st Person Name: "), int(input("Days in Flat: ")))
mate2 = Flatmate(input("2nd Person Name: "), int(input("Days in Flat: ")))

pdf = PDFReport(filename=f"{bill.period}.pdf")
pdf.generate(mate1, mate2, bill)

print("\nGenerating PDF..........")
print("\n PDF Created !!\n\n")

