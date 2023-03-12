from Rooms import roomsApp
from app.models import db, RoomData, PatientData

from flask import render_template
from flask import session
from flask import request
from flask import flash


@roomsApp.route('/', methods = ['GET','POST'])
def RoomsPage():
    if 'LoggedIn' in session:
        if session['LoggedIn']:
            id = session['id']

            if request.method == 'GET':
                return render_template('RoomsPage.html', data = getRoomsData())

            if request.method == 'POST':
                addRemoveRoomData(request.form)
                return render_template('RoomsPage.html', data = getRoomsData())


def getRoomsData():
    result = RoomData.query.all()
    data = {}
    if len(result) == 0:
        data = {
            'isPresent': 0
        }

    for i in result:
        data[i.id] = {
            'name': i.rname,
            'no': i.rno,
            'status': i.status,
            'allocatedTo': i.AllocatedTo
        }

    return data

def addRemoveRoomData(data):
    if data['hiddenValue'] == '0':
        r = RoomData(rname=data['rname'], rno=data['rno'], status = "Available", AllocatedTo = "None")
        db.session.add(r)
        db.session.commit()
        flash("Room added.", "success")

    elif data['hiddenValue'] == '1':
        r = RoomData.query.filter_by(rno = data['rno']).first()
        if r is None:
            flash("Room does not exist", "error")
        else:
            db.session.delete(r)
            db.session.commit()
            flash("Room removed.", "success")


    elif data['hiddenValue'] == '2':
        r = RoomData.query.filter_by(rno=data['rno']).first()
        if r is None:
            flash("Room does not exist", "error")
        elif r.status != "Available":
            p = PatientData.query.filter_by(allocatedRoom = data['rno']).first()
            p.allocatedRoom = 0

            r.status = "Available"
            r.AllocatedTo = 'None'

            db.session.commit()
            flash("Room status changed.", "success")

        elif r.status == "Available":
            flash("Room status is already Available.", "success")
