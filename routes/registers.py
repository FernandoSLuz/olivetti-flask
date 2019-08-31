import sys
import os
import time

import flask
import requests

blueprint = flask.Blueprint('registers', __name__)

@blueprint.route('/registers', methods=[ 'GET' ])
def registers():
    context = {
        'title':'Hacka | Update'
    }
    return flask.render_template('registers.html', context=context)