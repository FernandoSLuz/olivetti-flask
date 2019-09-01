# -*- coding: utf-8 -*-
import sys
import os
import time
import json

import flask
from flask import request
import requests as req
blueprint = flask.Blueprint('webhook', __name__)

class UserStep():
    nome_funcionario = ""
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
    tempUserStep.passo = 'B1'
    UserSteps.append(tempUserStep)
    return tempUserStep

def sendMessage(userTosendMessage, messageBody):
    print(userTosendMessage.telefone + " -- " + messageBody)
    url = "https://api.wassenger.com/v1/messages"


    payload = "{\"phone\":\""+userTosendMessage.telefone+"\",\"message\":\""+messageBody+"\"}"
    headers = {
        'content-type': "application/json",
        'token': "905bd94b9d3a26df733849887c838b9cc5ee1538b72fb1937edf027d5b7b71c71b2c54f1c894e4a2"
        }

    res = req.request("POST", url, data=payload, headers=headers)
    res.json() if res.status_code == 200 else []
    print(res.json())
    
def returnMessage(tempUserStep, recievedMessage):
    #print("*** Lenght = " + str(len(UserSteps))+ "*********** " + tempUserStep.telefone + " ********** " + tempUserStep.passo)
    if tempUserStep.passo == 'B1':
        sendMessage(tempUserStep, "Ola! Informe seu nome completo, por favor:")
        #print("Novo passo = B1")
        tempUserStep.passo = "B2"
    elif tempUserStep.passo == 'B2':
        sendMessage(tempUserStep, "Muito bem, "+recievedMessage+"./nVoce poderia me dizer em qual loja trabalha?")
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
    recievedPhoneStr = str(form['data']['fromNumber'])
    recievedMessage = str(form['data']['body'])
    tempUserStep = processNumber(recievedPhoneStr)
    returnMessage(tempUserStep, recievedMessage)
    context = {
        'title':'webhook | message recieved and processed'
    }
    return context