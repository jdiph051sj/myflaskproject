from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, Flask 1..2..>>3 DeployAgain1-223'
