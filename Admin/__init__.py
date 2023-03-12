from flask import Blueprint

adminApp = Blueprint('Admin', __name__,
                  template_folder='templates', static_folder='static')

from Admin import routes