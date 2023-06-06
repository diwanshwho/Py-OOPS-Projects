from fpdf import FPDF
import os,webbrowser

class PDFReport:
    """
    Class to create PDF report along with necessary information.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        month_dict = {'01':'January', 
                      '02':'February', 
                      '03':'March',
                      '04':'April',
                      '05':'May',
                      '06':'June',
                      '07':'July',
                      '08':'August',
                      '09':'September',
                      '10':'October',
                      '11':'November',
                      '12':'December'}
        # setting up the pdf properties
        pdf = FPDF(orientation="L", unit="pt", format="A4")
        pdf.set_font(family="Arial", size= 20, style="BU")
        pdf.add_page()

        # Adding the header
        pdf.cell(w=0, h=50, txt="Bill Splitter", align="C",ln=1)

        # Changing text properties and adding period 
        pdf.set_font(family="Arial", size=8, style= "B")
        pdf.cell(w=0, h=20, txt= month_dict[str(bill.period[-2:])]+' '+str(bill.period[:4]), align="R", ln=1)
        pdf.cell(w=0,h=10,ln=1)

        # Changing text properties again and adding Table heading
        pdf.set_font(family="Arial", size=12, style= "B")
        pdf.cell(w=230, h=30, txt="Flatmate", align="C", border=1)
        pdf.cell(w=150, h=30, txt="Days in Flat", align="C",border=1)
        pdf.cell(w=150, h=30, txt="Payment", align="C",border=1,ln=1)
        
        # Adding content 
        pdf.set_font(family="Arial", size=10)
        pdf.cell(w=0, h=10, ln=1)
        pdf.cell(w=230, h=20, txt=flatmate1.name, align="C")
        pdf.cell(w=150, h=20, txt=str(flatmate1.days), align="C")
        pdf.cell(w=150, h=20, txt=str(round(flatmate1.pays(bill,flatmate2))), align="C",ln=1)
        pdf.cell(w=230, h=20, txt=flatmate2.name, align="C")
        pdf.cell(w=150, h=20, txt=str(flatmate2.days), align="C")
        pdf.cell(w=150, h=20, txt=str(round(flatmate2.pays(bill,flatmate1))), align="C",ln=1)

        os.chdir('Bill_Splitter_WebApp\reports')
        pdf.output(self.filename)

        #To open pdf file automatically (only locally)
        # webbrowser.open(self.filename)
