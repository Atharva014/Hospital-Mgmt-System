from flask import Blueprint

patientApp = Blueprint('Patient', __name__,
                       template_folder='templates', static_folder='static')

from Patient import routes
