from flask import Flask, render_template, request, url_for, redirect, send_file
from pytube import YouTube

app = Flask(__name__)
app.config['SECRET_KEY'] = "HolaGente"

def download(url):
     video = url.streams.first()
     filepath = video.download()
     return filepath

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = YouTube(request.form.get('url'))
        filepath = download(url)
        return render_template('ver_video.html', filetitle = url.title, filepath = filepath)
    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def descargar_video():
    if request.method == 'POST':
        filepath = request.form.get('filepath')
        return send_file(filepath, as_attachment = True)
    return redirect(url_for('index'))
