from flask import Flask, current_app, render_template, request, redirect, send_from_directory, url_for, flash, send_file
from werkzeug.utils import secure_filename
from src import manager
from src.manager import output_file
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DOWNLOAD_FOLDER'] = 'downloads'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        uploaded_file = request.files['uploadname']
        secure_file = secure_filename(uploaded_file.filename)
        if secure_file != '':
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_file))
        # remove any existing file in downloads folder
        try:
            os.remove(os.path.join(app.config['DOWNLOAD_FOLDER'], output_file))
        except FileNotFoundError:
            pass
        # call to backend; this function will place the output file in the downloads folder
        manager.main(os.path.join(app.config['UPLOAD_FOLDER'], secure_file))
        # remove file from uploads folder
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], secure_file))
        return redirect(url_for('result'))
    return render_template('result.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/result/<path:filename>', methods=['GET','POST'])
def download(filename):
    downloads = os.path.join(current_app.root_path, app.config['DOWNLOAD_FOLDER'])
    return send_from_directory(downloads, filename, as_attachment=True)

if __name__ == '__main__':
    app.run()
