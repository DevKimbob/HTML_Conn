from flask import Flask, json
import socket, os

app = Flask(__name__)

print('Container name : ', socket.gethostname())
print('Container IP : ', socket.gethostbyname(socket.gethostname()), end='\n\n')

file = open('version.txt', 'r')
version = file.read().split('\n')[0].split('=')[1]
file.close()

@app.route("/")
def hello_world():
    html = f"Version : {version}\nContainer name : {socket.gethostname()}\nContainer IP : {socket.gethostbyname(socket.gethostname())}\n"
    # html = f"<body style='background-color:{os.environ.get('BG_COLOR')};'>\
    # <h1 style='color:{os.environ.get('FONT_COLOR')}'>{os.environ.get('CUSTOM_HEADER')}</h1> \
    # <h2 style='color:{os.environ.get('FONT_COLOR')};'>Hello World! Served from <b>{socket.gethostname()}</b></h2></body>"
    return html
