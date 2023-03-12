from datetime import datetime

from Dashboard import dboard
from app.models import db, LoginTable, AppointmentData

import datetime

from flask import render_template
from flask import redirect, url_for
from flask import session
from flask import request
from flask import flash

@dboard.route('/', methods=['GET', 'POST'])
def Dashboard():
    if 'LoggedIn' in session:
        if session['LoggedIn']:
            id = session['id']

            if request.method == 'GET':
                return render_template('Dashboard.html', data = getAppointmentData())

            if request.method == 'POST':
                addAppointment(request.form)
                flash("Appointment added.")
                return render_template('Dashboard.html', data = getAppointmentData())

    else:
        return redirect(url_for('HomeLogin'))


@dboard.route('/Logout', methods=['POST'])
def Logout():
    id = session['id']
    ldata = LoginTable.query.get(id)
    ldata.status = 'Offline'
    db.session.commit()
    return redirect(url_for('HomeLogin'))

def addAppointment(data):
    dateTimeSplit = data['time'].split('T')
    a = AppointmentData(pname = data['pname'], page = data['page'], pno = data['pno'], appointment = data['for'], appointmentDate = dateTimeSplit[0], appointmentTime = dateTimeSplit[-1])
    db.session.add(a)
    db.session.commit()

def getAppointmentData():
    todayDate = str(datetime.datetime.now()).split(" ")
    result = AppointmentData.query.filter_by(appointmentDate = todayDate[0]).all()
    aData = {}
    for i in result:
        aData[i.id] = {
            'name': i.pname,
            'no': i.pno,
            'appointmentFor': i.appointment,
            'time': i.appointmentTime
        }

    return aData
