import sys
import os
import time
import logging

import flask
import requests

from routes.auth import blueprint as auth_blueprint
from routes.jenkins import blueprint as jenkins_blueprint
from routes.docker import blueprint as docker_blueprint
from routes.gitlab import blueprint as gitlab_blueprint

logging.basicConfig(filename="/tmp/app.log",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(name)s\
                %(funcName)s - %(filename)s:%(lineno)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")

app = flask.Flask(__name__)

app.secret_key = 'secret'

app.register_blueprint(auth_blueprint)
app.register_blueprint(jenkins_blueprint)
app.register_blueprint(docker_blueprint)
app.register_blueprint(gitlab_blueprint)

@app.route('/')
def index():
    return ("Olá")

if __name__ == "__main__":

    root_module = os.path.abspath(os.path.curdir)
    sys.path.append(root_module)

    app.run(host='0.0.0.0')