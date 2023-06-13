from flask import Flask, json
import socket, os

app = Flask(__name__)

print('Container name : ', socket.gethostname())
print('Container IP : ', socket.gethostbyname(socket.gethostname()), end='\n\n')

@app.route("/")
def hello_world():
    html = f"Version : 1.2.0\nContainer name : {socket.gethostname()}\nContainer IP : {socket.gethostbyname(socket.gethostname())}\n"
    # html = f"<body style='background-color:{os.environ.get('BG_COLOR')};'>\
    # <h1 style='color:{os.environ.get('FONT_COLOR')}'>{os.environ.get('CUSTOM_HEADER')}</h1> \
    # <h2 style='color:{os.environ.get('FONT_COLOR')};'>Hello World! Served from <b>{socket.gethostname()}</b></h2></body>"
    return html
