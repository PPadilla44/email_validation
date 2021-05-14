from flask_app import app
from flask import render_template,redirect,request,session,flash

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template("index.html")

import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/create', methods=['POST'])
def create():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("INVALID EMAIL ADDRESS")
        return redirect('/')
    for e in Email.show_all():
        if request.form['email'] == e['email']:
            flash("EMAIL ADDRESS ALREADY IN USE")
            return redirect('/')

    email = Email.submit(request.form)
    return redirect(f'/success/{email}')

@app.route('/success/<emailid>')
def success(emailid):
    data = {
        'emailid': emailid
    }
    return render_template("success.html",email=Email.show(data), emails=Email.show_all())

@app.route('/delete/<emailid>')
def delete(emailid):
    data = {
        'emailid': emailid
    }
    Email.delete(data)
    return redirect('/')
