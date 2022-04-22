from flask import Blueprint

app_dashboard_init = Blueprint('dashboard', __name__, static_folder='static', template_folder='templates')

from app_center.process.dashboard import view_dashboard