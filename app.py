from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)
app.config['SECRET_KEY'] = "HolaGente"

def download(url):
     video = url.streams.first()
     video.download()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = YouTube(request.form.get('url'))
        download(url)
    return render_template('index.html')
