from flask import Flask, render_template, request, url_for, redirect, send_file, session
from pytube import YouTube
from os import remove, path

app = Flask(__name__)
app.config['SECRET_KEY'] = "HolaGente"

"""
def download(url):
     video = url.streams.first()
     filepath = video.download()
     return filepath
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    if request.method == 'POST':
        url = YouTube(request.form.get('url'))
        filepath = download(url)
        return render_template('ver_video.html', filetitle = url.title, filepath = filepath)
    """
    if request.method == 'POST':
        session['link'] = request.form.get('url')
        url = YouTube(session['link'])
        return render_template('ver_video.html', url = url)
    return render_template('index.html')

@app.route('/ver-video', methods=['GET', 'POST'])
def ver_video():
    if request.method == 'POST':
        url = YouTube(session['link'])
        itag = request.form.get('itag')
        video = url.streams.get_by_itag(itag)
        filename = video.download()
        return send_file(filename, as_attachment = True)

        # if path.exists(filename):
        #     remove(filename)
            
        # return True
    else:
        return redirect(url_for('index'))
    """
    if request.method == 'POST':
        filepath = request.form.get('filepath')
        return send_file(filepath, as_attachment = True)
    """
