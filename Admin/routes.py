from Admin import adminApp
from app.models import db, PatientData, LoginTable

from flask import render_template
from flask import session
from flask import request
from flask import flash
from flask import redirect, url_for

@adminApp.route('/', methods = ['GET', 'POSt'])
def AdminPage():
    if 'LoggedIn' in session:
        if session['LoggedIn']:
            id = session['id']

            if request.method == 'GET':
                return render_template('AdminPage.html', data = getAllData())

            if request.method == 'POST':
                return redirect(url_for('Admin.AddAdmin'))


def getAllData():
    result = PatientData.query.all()
    data = {}
    if len(result) == 0:
        pdata = {
            'isPresent': 0
        }

    for i in result:
        data[i.id] = {
            'name': i.pname,
            'bdate': i.bdate,
            'no': i.pno,
            'email': i.email,
            'address': i.address,
            'injury': i.injury,
            'accident': i.accident,
            'disease': i.disease,
            'other': i.other,
            'allocatedRoom': i.allocatedRoom,
            'time': (i.time.split(" "))[0]
        }
    return data

