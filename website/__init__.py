from flask import Flask


def create_app():
    #__name__ = The __name__ variable in Python is a special built-in variable that 
    # stores the name of the current module. It is often used to determine whether a 
    # Python script is being run directly or being imported as a module in another script. 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dgjasbj jasjb'
    
    from .views import views
    from .auth import auth
    #A Blueprint is a way to organize a group of related views and other code. 
    #Rather than registering views and other code directly with an application, 
    #they are registered with a blueprint. Then the blueprint is registered with 
    #the application when it is available in the factory function.
    app.register_blueprint(views, url_prefix = '/')
    #we are using prepfix as '/' if we use any name e.g. /auth the link will become /auth/login
    app.register_blueprint(auth, url_prefix = '/')
    return app