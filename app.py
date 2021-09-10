from flask import Flask, send_from_directory
import os 

app = Flask(__name__)

@app.route('/')
def index(): 
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir
    return send_from_directory(filepath, 'Resume.pdf')