import sys
import os
import time
import json

import flask
import requests
from flask import request

blueprint = flask.Blueprint('webhook', __name__)

@blueprint.route('/webhook', methods=[ 'GET' ])
def webhook():
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    print(res)
    context = {
        'title':'webhook | Update'
    }
    return context