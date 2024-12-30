from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "hjhjsdahhds"
socketio = SocketIO(app)
users = {}


@app.route("/", methods=["GET", "POST"])
def home():
    # session.clear()
    if (request.method == "POST"):
        if (request.form.get('formname') == "login"):
            username = request.form.get('username')
            session['username'] = username
        if (request.form.get('formname') == "logout"):
            session.clear()

    username = session.get('username')
    return render_template("index.html", username=username)


if __name__ == "__main__":

    socketio.run(app, debug=True)
