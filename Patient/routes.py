from Patient import patientApp
from app.models import db, PatientData, RoomData

from flask import render_template
from flask import session
from flask import request
import datetime
from flask import flash

@patientApp.route('/', methods = ['GET', 'POST'])
def PatientPage():
    if 'LoggedIn' in session:
        if session['LoggedIn']:
            id = session['id']

            if request.method == 'GET':
                return render_template('PatientPage.html', data = getPatientData())

            if request.method == 'POST':
                addPatientData(request.form)
                return render_template('PatientPage.html', data = getPatientData())


def addPatientData(data):
    p = PatientData(pname = data['pname'], bdate = data['bdate'], pno = data['pno'], email = data['email'],
                    address = data['addr'], injury = data['injury'], accident = data['accident'], disease = data['disease'],
                    other = data['other'], allocatedRoom = data['roomNo'], time = str(datetime.datetime.now()))
    db.session.add(p)

    r = RoomData.query.filter_by(rno = data['roomNo']).first()
    r.status = "Not Available"
    r.AllocatedTo = data['pname']
    db.session.commit()
    flash("Patient Data Added.", "success")

def getPatientData():
    result = PatientData.query.all()
    data, pdata = {}, {}
    if len(result) == 0:
        pdata = {
            'isPresent': 0
        }

    for i in result:
        pdata[i.id] = {
            'name': i.pname,
            'no': i.pno,
            'injury': i.injury,
            'accident': i.accident,
            'disease': i.disease,
            'other': i.other,
            'allocatedRoom': i.allocatedRoom,
            'time': (i.time.split(" "))[0]
        }
    roomList = getRoomList()
    data['roomList'] = roomList
    data['pdata'] = pdata
    return data

def getRoomList():
    l = []
    r = RoomData.query.filter_by(status='Available').all()
    if len(r) == 0:
        l = 0
    else:
        for i in r:
            l.append(i.rno)

    return l
