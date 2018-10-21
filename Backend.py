from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from NodeStuff import SensorNodeHandler

import random
class SensorNodeCluster:
        pass
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
app.config["TEMPLATES_AUTO_RELOAD"] = True

async_mode = "threading"
Verbose = True
socketio = SocketIO(app, async_mode=async_mode)

if not Verbose:
	import logging
	log = logging.getLogger("werkzeug")
	log.setLevel(logging.ERROR)

@app.route("/")
def hello():
    data = [[random.randint(0,1000),random.randint(0,600),random.randint(0,20)] for i in range(800)]
    return render_template(
        'index.html',data=data)
         
if __name__ == "__main__":
    socketio.run(app,host="0.0.0.0")