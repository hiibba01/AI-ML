from flask import Flask
'''It will be an instance of Flask Class which will be ur WSGI (WEB SERVER GATEWAY INTERFACE) application'''
#WSGI application-

app = Flask(__name__)  # __name__ is a special variable which will be set to __main__ when we run this file directly

@app.route("/")
def welcome():
    return "Welcome to Flask!HELLOOOOO HIIIIII HIBAAAA"

@app.route("/about")
def about():
    return "This is about page"

if __name__ == "__main__":  #this is entry point of any py filee
    app.run(debug=True)  
    #debug=True  THIS IS USED FOR DEVELOPMENT PURPOSES, IT WILL RELOAD THE SERVER AUTOMATICALLY WHENEVER WE MAKE CHANGES IN THE CODE.