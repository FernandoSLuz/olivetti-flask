import sys
import os
import time
import json
import dialogflowBackend as dfb

import flask


from flask import Blueprint


blueprint = flask.Blueprint('wassengerBackend', __name__)


def sendWassengerMessage(phoneNumber, message):
    import requests as req
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

@blueprint.route('/sendmessage', methods=[ 'GET'])
def sendmessage():
    dfb.detect_intent_audio("chatbot-olivetti","111111111111", "en-us")
    return "done"
########################################################################################################################################

@blueprint.route('/recieveWassengerMessage', methods=[ 'POST', 'GET' ])
def recievemessage():
    from flask import request
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    recievedMessage = ""
    recievedPhone = ""
    if(form['data']['chat']['contact']['type']):
        if(str(form['data']['chat']['contact']['type']) == 'user'):
            print("1")
            recievedMessage = str(form['data']['body'])
            recievedPhone = str(form['data']['fromNumber'])
            print("message recieved")
            #CHANGELATER
            dialogCallBackMessage = dfb.checkNumberStatus(recievedPhone, recievedMessage)
            print(dialogCallBackMessage)
            sendWassengerMessage(recievedPhone, dialogCallBackMessage)
            #sendMessageToWassenger(recievedPhoneStr, recievedMessage)
            return "200"
        else:
            return("---------------> message is not from user. Type = " + str(form['data']['chat']['contact']['type']))
    else:
        return('key dos not exist.')