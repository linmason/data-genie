from flask import Flask, current_app, render_template, request, redirect, send_from_directory, url_for, flash, send_file
from werkzeug.utils import secure_filename
from src import manager
import os
import zipfile

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DOWNLOAD_FOLDER'] = 'downloads'
app.config['SECRET_KEY'] = '49d96fab16d1c511f270a77c3600b13be04b7baf1aee5f7a8f3eb2aca6b01d3f'

def _rm_all_files(dir):
    filelist = [f for f in os.listdir(dir)]
    for f in filelist:
        if not f.startswith(".gitignore"):
            os.remove(os.path.join(dir, f))

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
        if uploaded_file.filename == '':
            flash('No selected file')
            return redirect(request.url) #code reaches here; flash does not do anything
        if secure_file != '':
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_file))
        # remove any existing file in downloads folder
        _rm_all_files(app.config['DOWNLOAD_FOLDER'])
        # call to backend; this function will place the output file in the downloads folder
        manager.main(os.path.join(app.config['UPLOAD_FOLDER'], secure_file))
        # remove file from uploads folder
        _rm_all_files(app.config['UPLOAD_FOLDER'])
        return redirect(url_for('result'))
    return render_template('result.html')

@app.route('/result')
def result():
    return render_template('result.html')

#The following is for downloading a single file.
#@app.route('/result/<path:filename>', methods=['GET','POST'])
#def download(filename):
#    downloads = os.path.join(current_app.root_path, app.config['DOWNLOAD_FOLDER'])
#    return send_from_directory(downloads, filename, as_attachment=True)

@app.route('/download_all')
def download_all():
    files = request.files.getlist('file[]')
    zf = zipfile.ZipFile('datagenie.zip','w',zipfile.ZIP_DEFLATED)
    for root,dirs, files in os.walk('downloads/'):
        for file in files:
            zf.write('downloads/'+file)
    zf.close()
    return send_file('datagenie.zip', mimetype='zip', attachment_filename='datagenie.zip', as_attachment=True)

if __name__ == '__main__':
    app.run()
