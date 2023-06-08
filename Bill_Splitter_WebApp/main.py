from wtforms import Form, StringField, IntegerField, SubmitField
from flask import Flask, render_template, request, url_for, redirect
from splitter_files.flatmate import Bill,Flatmate
# from splitter_files.reports import PDFReport

app = Flask(__name__)

@app.route('/')
def HomePage():
    return render_template('home.html', title="Home")

@app.route('/bill')
def BillFormPage():
    form = BillForm()
    return render_template('billformpage.html', form=form, title="Bill Form")

@app.route('/result', methods=['POST','GET'])
def ResultPage():
    if request.method=='POST':
        bill_form = BillForm(request.form)

        bill = Bill(bill_form.amount.data, bill_form.bill_period.data)
        flatmate1 = Flatmate(bill_form.name1.data, bill_form.days1.data)
        flatmate2 = Flatmate(bill_form.name2.data, bill_form.days2.data)

        # PDFReport(str(bill_form.bill_period.data)+'.pdf').generate(flatmate1, flatmate2, bill)

        return render_template('result.html', title='Splitted Bill', form = bill_form ,
                               amount1 = round(flatmate1.pays(bill, flatmate2)),
                               amount2 = round(flatmate2.pays(bill, flatmate1)))

    return redirect(url_for('HomePage'))

class BillForm(Form):
    bill_period = StringField('Bill Month: ')
    amount = IntegerField("Bill Amount: ")

    name1 = StringField('Name: ')
    days1 = IntegerField('Days: ')

    name2 = StringField("Name: ")
    days2 = IntegerField("Days: ")

    button = SubmitField("Split Bill")

app.run(debug=True)


