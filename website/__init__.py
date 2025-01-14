from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "userdatabase.db"

def create_app():
    #__name__ = The __name__ variable in Python is a special built-in variable that 
    # stores the name of the current module. It is often used to determine whether a 
    # Python script is being run directly or being imported as a module in another script. 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dgjasbj jasjb'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    #A Blueprint is a way to organize a group of related views and other code. 
    #Rather than registering views and other code directly with an application, 
    #they are registered with a blueprint. Then the blueprint is registered with 
    #the application when it is available in the factory function.
    app.register_blueprint(views, url_prefix = '/')
    #we are using prepfix as '/' if we use any name e.g. /auth the link will become /auth/login
    app.register_blueprint(auth, url_prefix = '/')

    from .models import User, Note
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
    
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')