import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sample')
def sample():
    return render_template('sample.html')

@app.route('/salary')
def salary():
    file_prefix = "/Users/sks/seeeds/python/file_io/"
    input_file_name = file_prefix + "input.json"
    input_file = open(input_file_name)
    persons_list = json.load(input_file)
    input_file.close()
    return render_template('salary.html', persons=persons_list)