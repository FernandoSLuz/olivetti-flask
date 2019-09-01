import sys
import os
import time

import flask
import requests

blueprint = flask.Blueprint('webhook', __name__)

@blueprint.route('/webhook', methods=[ 'GET' ])
def webhook():
    context = {
        'title':'webhook | Update'
    }
    return context