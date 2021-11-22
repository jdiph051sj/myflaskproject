#Create a Flask/Python wep app
from flask import Flask 

#Create an instance of FLask
application = Flask(__name__)

#Create an end-point for the app
@application.route('/')

#Define a function
def hello_world():
    #Fucntion that returns a string
    return 'Hello, Flask App-->> Deploy1-2-3'
