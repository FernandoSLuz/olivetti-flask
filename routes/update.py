import sys
import os
import time

import flask
import requests

blueprint = flask.Blueprint('update', __name__)

@blueprint.route('/update', methods=[ 'GET' ])
def update():
    context = {
        'title':'Hacka | Update'
    }
    return flask.render_template('update.html', context=context)

@blueprint.route('/submitupdate', methods=[ 'POST' ])
def submitupdate():
    context = {
        'title':'Hacka | Pepe'
    }

    return flask.render_template('update.html', context=context)