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
    tempUserStep = UserStep()
    tempUserStep.telefone = str(numberRecieved)
    tempUserStep.passo = ""
    UserSteps.append(tempUserStep)
    return tempUserStep

def sendMessage(userTosendMessage, messageBody):
    print("")
    url = "https://api.wassenger.com/v1/messages"
    data = {
        'phone': userTosendMessage.telefone,
        'message': messageBody
    }
    headers = {
    'content-type': "application/json",
    'token': "905bd94b9d3a26df733849887c838b9cc5ee1538b72fb1937edf027d5b7b71c71b2c54f1c894e4a2"
    }

    requests.request("POST", url, data=data, headers=headers)

    
def returnMessage(tempUserStep):
    #print("*** Lenght = " + str(len(UserSteps))+ "*********** " + tempUserStep.telefone + " ********** " + tempUserStep.passo)
    if tempUserStep.passo == '':
        sendMessage(tempUserStep, "Bom dia")
        sendMessage(tempUserStep, "Mensagem 2")
        #print("Novo passo = B1")
        tempUserStep.passo = "B1"
    elif tempUserStep.passo == 'B1':
        sendMessage(tempUserStep, "Você mandou mensagem pela segunda vez")
        #print("Novo passo = B2")
        tempUserStep.passo = "B2"
    else:
        sendMessage(tempUserStep, "você \n mandou mensagem, \nagora respondo com quebra de linhas.\n\n\n\nterceira vez a propósito.")
        #print('B2 até agora!')
    
    for item in UserSteps:
        if item.telefone == tempUserStep.telefone:
            item.passo = tempUserStep.passo

    


@blueprint.route('/webhook', methods=[ 'POST', 'GET' ])
def webhook():
    form = request.get_json(silent=True, force=True)
    #res = (json.dumps(form, indent=3))
    #print(res)
    recievedPhoneStr = form['data']['fromNumber']
    tempUserStep = processNumber(str(recievedPhoneStr))
    returnMessage(tempUserStep)
    context = {
        'title':'webhook | message recieved and processed'
    }
    return context