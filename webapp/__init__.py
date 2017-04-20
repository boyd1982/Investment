from flask import Flask,redirect,url_for,render_template
from flask_principal import identity_loaded,UserNeed,RoleNeed
from config import DevConfig
from controllers.stock import stock_blueprint
from controllers.main import main_blueprint
from controllers.stock_solo import stocksolo_blueprint
from forms import CodeForm
from datetime import datetime
from extensions import login_manager,principals
from models import db,mongo
from flask_login import current_user



def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    #db.init_app(app)
    # @app.route('/')
    # def index():
    #     return redirect(url_for('blog.home'))
    login_manager.init_app(app)
    principals.init_app(app)
    db.init_app(app)
    mongo.init_app(app)
    app.register_blueprint(stock_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(stocksolo_blueprint)
    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender,identity):
        identity.user = current_user
        if hasattr(current_user,"username"):
            identity.provides.add(UserNeed(current_user.username))
        if hasattr(current_user,'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role))
    return app


