import sys
import os
import time
import json

import flask
from flask import request
import requests as req
from flask import Blueprint
import dialogflow
from google.protobuf import struct_pb2
import requests as req

blueprint = flask.Blueprint('dialogflowBackend', __name__)



def sendDialogflowMessage():
    print("change")

def checkNumberStatus(phone, message):
    print("status")
    url = "https://lighthouse-vms.appspot.com/users/check_status"
    payload = "{\"phone\":\""+phone+"\"}"
    res = req.request("POST", url, data=payload)
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    print(res)




@blueprint.route('/testintents_greetings', methods=[ 'POST'])
def testintents_greetings():
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    queryText = sendGreetings("chatbot-olivetti", str(form['sessionId']), str(form['message']), str(form['languageCode']))
    context = {
        "Fulfillment Text" : queryText
    }
    return(context)

@blueprint.route('/testintents', methods=[ 'POST'])
def testintents():
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    
    
    queryText =  detect_intent_texts("chatbot-olivetti", str(form['sessionId']), str(form['message']), str(form['languageCode']))
    context = {
        "Fulfillment Text" : queryText
    }
    return(context)

def sendGreetings(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    parameters = struct_pb2.Struct()
    parameters["name"] = 'Fernando'
    parameters["surname"] = 'Luz'
    
    query_input = {
        'event': {
            "name": "greetPerson",
            "parameters": parameters,
            "language_code": language_code
        }
    }
    response = session_client.detect_intent(
        session=session,
        query_input=query_input)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))
    return str(response.query_result.fulfillment_text)

def detect_intent_texts(project_id, session_id, text, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    import dialogflow_v2 as dialogflow2
    session_client = dialogflow2.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    text_input = dialogflow2.types.TextInput(
        text=text, language_code=language_code)

    query_input = dialogflow2.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))
    return str(response.query_result.fulfillment_text)