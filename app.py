from flask import Flask, render_template, request, redirect, url_for, session
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder='file')
CORS(app)

UPLOAD_FOLDER = "./file"
ALLOWED_EXTENSION = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def fileUpload():
    target = os.path.join(UPLOAD_FOLDER, 'test')
    if not os.path.isdir(target):
        os.mkdir(target)
    
    file = request.files['file']
    destination = "/".join([target, file.filename])
    file.save(destination)
    location = "http://localhost:5000/file/test/" + file.filename
    return {"location": location}


if __name__ == "__main__":
    app.run(debug=True)
