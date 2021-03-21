from flask import Flask, render_template, request, redirect, url_for, session, send_file
import os
from flask_cors import CORS, cross_origin
import pdfkit
from jinja2 import Template
import time

app = Flask(__name__, static_folder='file')
CORS(app)

# UPLOAD_FOLDER = "./file"
UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSION = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def fileUpload():
    target = os.path.join(UPLOAD_FOLDER, 'file')
    if not os.path.isdir(target):
        os.mkdir(target)
    
    file = request.files['file']
    print
    # destination = "/".join([target, file.filename])
    destination = os.path.join(target, file.filename)
    file.save(destination)
    location = "http://localhost:5000/file/" + file.filename
    return {"location": location, "name": file.filename, "size": "500"}
    # return {"location": location}

@app.route('/pdf', methods=['POST'])
def generatePDF():
    target = os.path.join(UPLOAD_FOLDER, 'file')
    if not os.path.isdir(target):
        os.mkdir(target)
        
    value = request.form.get("desc")
    rtemplate = Template(value)
    filename = str(int(round(time.time() * 1000))) + ".pdf"
    destination = os.path.join(target, filename)
    pdfkit.from_string(rtemplate.render(requestor_email='gopalakrishnan@kissflow.com'), destination)
    return send_file(destination, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, ssl_context="adhoc")
