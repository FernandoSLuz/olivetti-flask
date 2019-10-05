import sys
import os
import time
import json

import flask
from flask import request
import requests as req
from flask import Blueprint

blueprint = flask.Blueprint('wassengerBackend', __name__)

def sendMessageToWassenger(phoneNumber, message):
    url = "https://api.wassenger.com/v1/messages"
    payload = "{\"phone\":\""+phoneNumber+"\",\"priority\":\"urgent\",\"message\":\""+message+"\"}"
    headers = {
        'content-type': "application/json",
        'token': "905bd94b9d3a26df733849887c838b9cc5ee1538b72fb1937edf027d5b7b71c71b2c54f1c894e4a2"
        }
    res = req.request("POST", url, data=payload, headers=headers)
    res.json() if res.status_code == 200 else []
    return res.status_code
    #print(res.json())

@blueprint.route('/sendmessage', methods=[ 'POST'])
def sendmessage():
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    #print(res)
    phone = str(form['phone'])
    message = str(form['message'])
    statusCode = sendMessageToWassenger(phone, message)
    context = {
        'phone': phone,
        'message': message,
        'status': statusCode
    }
    return context
########################################################################################################################################

@blueprint.route('/recieveFromWassenger', methods=[ 'POST', 'GET' ])
def recievemessage():
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))

    recievedPhoneStr = str(form['data']['fromNumber'])
    if(form['data']['chat']['contact']['type']):
        if(str(form['data']['chat']['contact']['type']) == 'user'):
            print(res)
        else:
            print("---------------> message is not from user. Type = " + str(form['data']['chat']['contact']['type']))
    else:
        print('key dos not exist.')
    #recievedMessage = str(form['data']['body'])
    #phones = bd.SelectAllPhones()
    #context = {
    #    'wassengerPhone': recievedPhoneStr,
    #    'wassengerMessage': recievedMessage
    #}
    #return context
    return "200"