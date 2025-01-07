from website import create_app

app = create_app()
#we can run application  only from __main__.py 
if __name__ == '__main__':
    app.run(debug=True)