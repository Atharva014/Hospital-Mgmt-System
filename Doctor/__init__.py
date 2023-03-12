from flask import Blueprint

doctorApp = Blueprint('Doctor', __name__,
                      template_folder='templates', static_folder='static')

from Doctor import routes
