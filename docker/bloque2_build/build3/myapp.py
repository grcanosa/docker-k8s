from datetime import datetime
import os
from flask import Flask

import time

app = Flask(__name__)

start = time.time()

@app.route('/hello')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello, World!'

@app.route('/')
def main():
    """Return a current datetime"""
    return f'My flask app is running at {datetime.now()}'

@app.route('/<name>')
def hello_name(name):
    """Return a personalized greeting."""
    return f'Hello, {name}!'

@app.route("/myenv")
def myenv():
    """Return a current datetime"""
    return f'My flask app is running at has env variable {os.environ.get("MYENV","DEFAULT_VALUE")}'

@app.route("/uptime")
def uptime():
    """Return a current datetime"""
    return f'My flask app is running for {time.time()-start} seconds'

@app.route("/plus")
def plus():
    """Return a current datetime"""
    plus = 0
    if os.path.exists("plus.txt"):
        with open("plus.txt","r") as f:
            plus = int(f.read())
    plus += 1
    with open("plus.txt","w") as f:
        f.write(str(plus))            
    return f'My plus.txt file is set to {plus}'

@app.route("/getplus")
def getplus():
    """Return current plus.txt file value"""
    plus = 0
    if os.path.exists("plus.txt"):
        with open("plus.txt","r") as f:
            plus = int(f.read())
    return f'My plus.txt file is set to {plus}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)