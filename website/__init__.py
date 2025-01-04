from flask import Flask

def create_app():
    #__name__ = The __name__ variable in Python is a special built-in variable that 
    # stores the name of the current module. It is often used to determine whether a 
    # Python script is being run directly or being imported as a module in another script. 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dgjasbj jasjb'

    return app