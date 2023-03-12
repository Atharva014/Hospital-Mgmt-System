from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LoginTable(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(10), nullable = False)

    def __repr__(self):
        return '<User %r>' % self.id

class AppointmentData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(50), nullable=False)
    page = db.Column(db.Integer, nullable=False)
    pno = db.Column(db.BigInteger, nullable=False)
    appointment = db.Column(db.String(100), nullable=False)
    appointmentDate = db.Column(db.String(20), nullable=False)
    appointmentTime = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

class DoctorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dname = db.Column(db.String(50), nullable=False)
    bdate = db.Column(db.String(20), nullable=False)
    pno = db.Column(db.BigInteger, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    education = db.Column(db.String(50), nullable=False)
    speciality = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

class RoomData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rname = db.Column(db.String(50), nullable=False)
    rno = db.Column(db.BigInteger, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    AllocatedTo = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

class PatientData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(50), nullable=False)
    bdate = db.Column(db.String(20), nullable=False)
    pno = db.Column(db.BigInteger, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    injury = db.Column(db.String(200), nullable=False)
    accident = db.Column(db.String(200), nullable=False)
    disease = db.Column(db.String(200), nullable=False)
    other = db.Column(db.String(200), nullable=False)
    allocatedRoom = db.Column(db.BigInteger, nullable=False)
    time = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id
