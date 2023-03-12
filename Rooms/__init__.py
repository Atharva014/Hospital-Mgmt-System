from flask import Blueprint

roomsApp = Blueprint('Rooms', __name__,
                     template_folder='templates', static_folder='static')

from Rooms import routes
