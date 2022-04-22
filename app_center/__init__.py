from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig
from flask_login import LoginManager, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink

from flask_mysqldb import MySQL
import MySQLdb.cursors


# import extensions instance
db = SQLAlchemy()
migrate = Migrate()
mysql = MySQL()
curMysql = MySQLdb.cursors.DictCursor

def center_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config["DEBUG"] = True   


    app.config['MYSQL_HOST']='localhost'  # dikoneksikan dengan database
    app.config['MYSQL_USER']='root'
    app.config['MYSQL_PASSWORD']='666666'
    # app.config['MYSQL_PASSWORD']=''
    app.config['MYSQL_DB']='kalung_db'

    # initialize extension instances
    mysql.init_app(app)
    mysql.app = app

    
    # initialize extension instances
    db.init_app(app)
    db.app = app
    
    # initialize extension instances
    migrate.init_app(app, db)
    migrate.app = app  
    
    
    from app_center.authentication.login import model, controller
    
    
    admin = Admin(app, name='Control Panel', template_mode='bootstrap4', index_view=model.DashboardView())
    admin.add_view(model.Controller(model.User, db.session, name='User'))
    # admin.add_view(ModelView(model_elo.m_jenis_kawat, db.session, name='Jenis Kawat'))
    # admin.add_view(ModelView(model_elo.m_diameter_kawat, db.session, name='Diameter Kawat'))
    # admin.add_view(ModelView(model_elo.m_tebal_kawat, db.session, name='Tebal Kawat'))
    # admin.add_view(ModelView(model_elo.m_kadar, db.session, name='Kadar'))
    # admin.add_view(ModelView(model_elo.m_alloy, db.session, name='Alloy'))
    
    login_manager = LoginManager()
    login_manager.init_app(app)  
    login_manager.login_view = 'login.login'
    
    
    from app_center.authentication.login import model
    
    @login_manager.user_loader
    def load_user(user_id):
      # since the user_id is just the primary key of our user table, use it in the query for the user
      return model.User.query.get(int(user_id))
    
    # @login_manager.unauthorized_handler
    # def unauthorized_handler():
    #   return render_template('home/page-403.html'), 403

    
    
    # ----------register blueprints of applications-----------
    
    # LOGIN
    from app_center.authentication.login import app_login_init as login
    app.register_blueprint(login)
    
    # HOME
    from app_center.authentication.home import app_home_init as home
    app.register_blueprint(home)
    
    # HOME
    from app_center.process.dashboard import app_dashboard_init as dashboard
    app.register_blueprint(dashboard)
    
    # # MASTER EXIT
    # from app_center.exit.master import app_master as master
    # app.register_blueprint(master)
    
    
    # # RUSAK DAN REPARASI
    # from app_center.exit.rusak_reparasi import app_rusak_reparasi as rusak_reparasi
    # app.register_blueprint(rusak_reparasi)

    # # ALGO
    # from app_center.process.algo import app_algo_init as algo
    # app.register_blueprint(algo)
    
    
    # from app_hollows.entry.dummy_xxx import app_xxx_init as xxx
    # app.register_blueprint(xxx)
    

    
    return app
