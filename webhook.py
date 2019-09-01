import sys
import os
import time
import json

import flask
import requests
from flask import request

blueprint = flask.Blueprint('webhook', __name__)

class UserStep():
    telefone = ""
    setor = ""
    loja = ""
    passo = ""

UserSteps = [] 


@blueprint.route('/webhook', methods=[ 'POST', 'GET' ])
def webhook():
    form = request.get_json(silent=True, force=True)
    #res = (json.dumps(form, indent=3))
    #print(res)
    recievedPhoneStr = form['data']['fromNumber']
    phoneStr = ""
    for item in UserSteps:
        if item.telefone == str(recievedPhoneStr):
            phoneStr = str(recievedPhoneStr)
    if phoneStr == "":
        print('not found, adding number ' + str(recievedPhoneStr))
        phoneStr = str(recievedPhoneStr)
        tempUserStep = UserStep
        tempUserStep.telefone = phoneStr
        UserSteps.append(tempUserStep)
    else:
        print('number exists! ' + phoneStr)

    context = {
        'title':'webhook | ' + phoneStr
    }
    return context