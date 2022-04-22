from flask import Blueprint

app_home_init = Blueprint('home', __name__, static_folder='static', template_folder='templates')

from app_center.authentication.home import view