from flask import Flask
from app.config import Config
from app.models import db

app = Flask(__name__)
app.secret_key = "atharva"

app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

from app import routes
from Dashboard import dboard
from Admin import adminApp
from Doctor import doctorApp
from Patient import patientApp
from Rooms import roomsApp

app.register_blueprint(dboard, url_prefix = "/Dashboard")
app.register_blueprint(adminApp, url_prefix = "/Admin")
app.register_blueprint(doctorApp, url_prefix = "/Doctor")
app.register_blueprint(patientApp, url_prefix = "/Patient")
app.register_blueprint(roomsApp, url_prefix = "/Rooms")
