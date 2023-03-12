from Doctor import doctorApp
from app.models import db, DoctorData

from flask import render_template
from flask import session
from flask import request
from flask import flash


@doctorApp.route('/', methods=['POST', 'GET'])
def DoctorPage():
    if 'LoggedIn' in session:
        if session['LoggedIn']:
            id = session['id']

            if request.method == 'GET':
                return render_template('DoctorPage.html', data = getDoctorData())

            if request.method == 'POST':
                addRemoveDoctorData(request.form)
                return render_template('DoctorPage.html', data = getDoctorData())


def addRemoveDoctorData(data):
    if data['hiddenValue'] == '0':
        d = DoctorData(dname = data['dname'], bdate = data['bdate'], pno = data['pno'], email = data['email'],
                       address = data['addr'], education = data['edu'], speciality = data['Speciality'])
        db.session.add(d)
        db.session.commit()
        flash("Doctor added.")

    elif data['hiddenValue'] == '1':
        d = DoctorData.query.filter_by(dname=data['dname']).first()
        if d is None:
            flash("Doctor does not exist", "error")
        else:
            db.session.delete(d)
            db.session.commit()
            flash("Room removed.", "success")

def getDoctorData():
    result = DoctorData.query.all()
    data = {}
    if len(result) == 0:
        data = {
            'isPresent': 0
        }

    for i in result:
        data[i.id] = {
            'name': i.dname,
            'no': i.pno,
            'email': i.email,
            'speciality': i.speciality
        }

    return data
