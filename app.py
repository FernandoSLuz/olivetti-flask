import sys
import os
import time

import flask
import requests

from routes.registers import blueprint as registers_blueprint
from routes.update import blueprint as update_blueprint


app = flask.Flask(__name__)

app.secret_key = 'secret'

app.register_blueprint(registers_blueprint)
app.register_blueprint(update_blueprint)

@app.route('/')
def index():
    context = {
        'title':'Hacka | Update'
    }
    return flask.render_template('index.html')
    #return context

if __name__ == "__main__":

    root_module = os.path.abspath(os.path.curdir)
    sys.path.append(root_module)

    app.run(host='0.0.0.0')