from flask import Flask, render_template, request
from flask_socketio import SocketIO
from main import bot

app = Flask(__name__)
app.config['SECRET KEY'] = '372jm3wfvmkwnvNCEKDMß©KEWJDBQWCMVRE'
socket_io = SocketIO(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == '__main__':
    socket_io.run(app, debug=True)
