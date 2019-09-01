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



def processNumber(numberRecieved):
    for item in UserSteps:
        if item.telefone == str(numberRecieved):
            print('number exists! ' + str(numberRecieved))
            return item
            
    print('not found, adding number ' + str(numberRecieved))
    tempUserStep = UserStep
    tempUserStep.telefone = str(numberRecieved)
    #tempUserStep.passo = ""
    UserSteps.append(tempUserStep)
    return tempUserStep

def returnMessage(tempUserStep):
    if tempUserStep.passo == '':
        print("Novo passo = B1")
        tempUserStep.passo = "B1"
    elif tempUserStep.passo == 'B1':
        print("Novo passo = B2")
        tempUserStep.passo = "B2"
    else:
        print('B2 até agora!')
    
    for item in UserSteps:
        if item.telefone == tempUserStep.telefone:
            item.passo = tempUserStep.passo
            
    return tempUserStep.passo


@blueprint.route('/webhook', methods=[ 'POST', 'GET' ])
def webhook():
    form = request.get_json(silent=True, force=True)
    #res = (json.dumps(form, indent=3))
    #print(res)
    recievedPhoneStr = form['data']['fromNumber']
    tempUserStep = processNumber(str(recievedPhoneStr))
    feedback = returnMessage(tempUserStep)
    context = {
        'title':'webhook | ' + tempUserStep.telefone
    }
    return context