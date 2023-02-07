
from flask import Flask
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

    
#Start Flask application in debug mode   
if __name__ == '__main__':
    app.debug = True
    app.run()
