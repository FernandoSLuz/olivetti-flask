import sys
import os
import time
import json

import flask
from flask import request
import requests as req
from flask import Blueprint
import bd

blueprint = flask.Blueprint('webhook', __name__)

class UserStep():
    nome_funcionario = ""
    telefone = ""
    setor = ""
    loja = ""
    passo = ""

UserSteps = [] 


def updateUserStep(tempUser):
    for item in UserSteps:
        if item.telefone == tempUser.telefone:
            item = tempUser
            return

def processNumber(numberRecieved):
    for item in UserSteps:
        if item.telefone == str(numberRecieved):
            #print('number exists! ' + str(numberRecieved))
            return item
    #print('not found, adding number ' + str(numberRecieved))
    tempUserStep = UserStep()
    tempUserStep.telefone = str(numberRecieved)
    tempUserStep.passo = ''
    UserSteps.append(tempUserStep)
    return tempUserStep

def sendMessageToLeader(leader, requester):
    url = "https://api.wassenger.com/v1/messages"

    messageBody = "Olá " + str(leader[1]) + "! um funcionário solicitou acesso à plataforma de serviços IntranetMall:\\n\\nNome: " + requester.nome_funcionario + "\\nTelefone: " + requester.telefone 
    
    payload = "{\"phone\":\""+str(leader[0])+"\",\"priority\":\"urgent\",\"message\":\""+messageBody+"\"}"
    headers = {
        'content-type': "application/json",
        'token': "905bd94b9d3a26df733849887c838b9cc5ee1538b72fb1937edf027d5b7b71c71b2c54f1c894e4a2"
        }

    res = req.request("POST", url, data=payload, headers=headers)
    res.json() if res.status_code == 200 else []
    #print(res.json())
def sendMessage(userTosendMessage, messageBody):
    #print(userTosendMessage.telefone + " -- " + messageBody)
    url = "https://api.wassenger.com/v1/messages"

    encodedMessage = str(messageBody.encode())
    payload = "{\"phone\":\""+userTosendMessage.telefone+"\",\"priority\":\"urgent\",\"message\":\""+encodedMessage+"\"}"
    headers = {
        'content-type': "application/json",
        'token': "905bd94b9d3a26df733849887c838b9cc5ee1538b72fb1937edf027d5b7b71c71b2c54f1c894e4a2"
        }

    res = req.request("POST", url, data=payload, headers=headers)
    res.json() if res.status_code == 200 else []
    #print(res.json())
    
def returnMessage(tempUserStep, recievedMessage):
    if(tempUserStep.passo == ''):
        bd.checkIfUserExists(tempUserStep)
    if tempUserStep.passo == 'B1':
        sendMessage(tempUserStep, "Ola! Informe seu nome completo, por favor:")
        #print("Novo passo = B1")
        tempUserStep.passo = "B2"
    elif tempUserStep.passo == 'B2':
        tempUserStep.nome_funcionario = recievedMessage
        updateUserStep(tempUserStep)
        sendMessage(tempUserStep, "Muito bem, "+tempUserStep.nome_funcionario+". \\n Voce poderia me dizer em qual setor trabalha?" + "\\n" + bd.SelectSetores())
        tempUserStep.passo = "B3"
    elif tempUserStep.passo == 'B3':
        tempUserStep.setor = bd.SelectSetores_Unique(int(recievedMessage))
        updateUserStep(tempUserStep)
        #print(tempUserStep.setor)
        sendMessage(tempUserStep, "Obrigado pelas confirmacoes, "+tempUserStep.nome_funcionario+". \\n Agora, voce poderia me dizer em qual loja trabalha?" + "\\n" + bd.SelectLojas(tempUserStep.setor))
        tempUserStep.passo = "B4"
    elif tempUserStep.passo == 'B4':
        if bd.searchByUsername(tempUserStep.nome_funcionario):
            tempUserStep.loja = bd.SelectLojas_Unique(int(recievedMessage))
            print("********************" + tempUserStep + "***********************")
            updateUserStep(tempUserStep)
            sendMessage(tempUserStep, "Muito bem, "+tempUserStep.nome_funcionario+"! agora que você está cadastrado(a), trarei as novidades do shopping Parque D. Pedro para você! \\nDigite a opção desejada:\\n1- Descontos\\n2- Avisos e Informações\\n3- Receber avisos automáticos\\n4- Desabilitar avisos automáticos")
            tempUserStep.passo = "A2"
        else:
            leader = bd.SearchLeader(tempUserStep)
            sendMessageToLeader(leader, tempUserStep)
            sendMessage(tempUserStep, "Infelizmente não localizei seu cadastro no Portal, mas já enviei uma solicitação ao seu líder e, assim que o cadastro for completado, você irá receber descontos e novidades aqui pelo Pepe!")
            tempUserStep.passo = ''
    elif tempUserStep.passo == 'A1':
        sendMessage(tempUserStep, "Olá, "+tempUserStep.nome_funcionario+"! Eu sou o Pepe e irei trazer as novidades do shopping Parque D. Pedro para você! \\nDigite a opção desejada:\\n1- Descontos\\n2- Avisos e Informações\\n3- Receber avisos automáticos\\n4- Desabilitar avisos automáticos")
        tempUserStep.passo = "A2"
    elif tempUserStep.passo == 'A2':
        if(recievedMessage == "1"):
            sendMessage(tempUserStep, "Feed de Noticias: \\n" + bd.SelectRequests())#bd.SelectLojas(tempUserStep.setor)
        elif(recievedMessage == "2"):
            sendMessage(tempUserStep, "V2 - Feed de Circular, em breve.")
        elif(recievedMessage == "3"):
            sendMessage(tempUserStep, "V2 - Habilitar/Desabilitar Promoções")
        elif(recievedMessage == "4"):
            sendMessage(tempUserStep, "V2 - Habilitar/Desabilitar Circular")
    else:
        sendMessage(tempUserStep, "fim das mensagens.")
        #print('B2 até agora!')
    
    for item in UserSteps:
        if item.telefone == tempUserStep.telefone:
            item.passo = tempUserStep.passo

    


@blueprint.route('/webhook', methods=[ 'POST', 'GET' ])
def webhook():
    print("Testeeee")
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    #print(res)
    recievedPhoneStr = str(form['data']['fromNumber'])
    recievedMessage = str(form['data']['body'])
    tempUserStep = processNumber(recievedPhoneStr)
    returnMessage(tempUserStep, recievedMessage)
    context = {
        'title':'webhook | message recieved and processed'
    }
    return context