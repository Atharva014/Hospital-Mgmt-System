from app import app
from app.models import db, LoginTable

from flask import render_template
from flask import redirect, url_for
from flask import session
from flask import request
from flask import flash


@app.route('/', methods=['GET', 'POST'])
def HomeLogin():
    session.clear()
    if request.method == 'POST':
        if isPresent(request.form):
            return redirect(url_for('Dashboard.Dashboard'))

    return render_template('LoginPage.html')

@app.route('/Register', methods = ['POST', 'GET'])
def Register():
    session.clear()
    if request.method == 'POST':
        if registerAdmin(request.form):
            flash("Registered Successfully.", "success")
            return render_template('RegisterPage.html')

    return render_template('RegisterPage.html')


def isPresent(data):
    flag = False
    ldata = LoginTable.query.filter_by(email=data['email']).first()
    if ldata is None:
        flash("Email does not exist", "error")
    else:
        if data['pass'] == ldata.password:
            session['LoggedIn'] = True
            session['id'] = ldata.id

            ldata.status = "Online"
            db.session.commit()

            flag = True
        else:
            flash("Invalid Email or Password.", "error")

    return flag

def registerAdmin(data):
    flag = False
    ldata = LoginTable.query.filter_by(email=data['email']).first()
    if ldata is not None:
        flash("Email already exist", "error")
    else:
        if data['pass'] == data['cpass']:
            if len(data['pass']) >= 8:
                l = LoginTable(name = data['aname'], email = data['email'], password = data['pass'], status = "Offline")
                db.session.add(l)
                db.session.commit()
                flag = True
            else:
                flash("Password should be minimum of 8 characters.", "error")
        else:
            flash("Password does not match.", "error")

    return flag
