import sys
import os
import time
import json

import flask

from flask import Blueprint
import dialogflow
from google.protobuf import struct_pb2



blueprint = flask.Blueprint('dialogflowBackend', __name__)


def checkNumberStatus(phoneRecieved, message):
    import requests as req
    url = "https://lighthouse-vms.appspot.com/users/check_status"
    payload = {
        'phone' : phoneRecieved
    }
    res = req.post(url, data=payload)
    form = res.json()
    try:
        phone = str(form['phone'])
        message = str(form['profile']) + " " + message
        conversationId = str(form['conversationId'])
        dialogCallBackMessage =  detect_intent_texts("chatbot-olivetti", conversationId, message, "en-us", phone)
        return dialogCallBackMessage
    except:
        print(form)
        return ""

@blueprint.route('/testintents_greetings', methods=[ 'POST'])
def testintents_greetings():
    from flask import request
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    queryText = sendGreetings("chatbot-olivetti", str(form['sessionId']), str(form['message']), str(form['languageCode']))
    context = {
        "Fulfillment Text" : queryText
    }
    return(context)

@blueprint.route('/testintents', methods=[ 'POST'])
def testintents():
    from flask import request
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

def detect_intent_texts(project_id, session_id, text, language_code, phone):
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

def detect_intent_audio(project_id, session_id, language_code):
    import os as operational
    import requests as reques

    print('Beginning file download with requests')

    url = 'https://api.wassenger.com/v1/io/5d9785b6036345001b5a85f8/files/5d98de1478a4b00028de8765/download?token=905bd94b9d3a26df733849887c838b9cc5ee1538b72fb1937edf027d5b7b71c71b2c54f1c894e4a2'
    r = reques.get(url)

    audioPath = '/home/fernando/olivetti/olivetti-flask/cat3.ogg'
    with open(audioPath, 'wb') as f:
        f.write(r.content)
    operational.system("ftransc -f flac cat3.ogg")
    audioPath = '/home/fernando/Documents/audios/cat3.flac'
    # Retrieve HTTP meta-data
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    """Returns the result of detect intent with an audio file as input.

    Using the same `session_id` between requests allows continuation
    of the conversaion."""
    import dialogflow_v2 as dialogflow2

    session_client = dialogflow.SessionsClient()

    # Note: hard coding audio_encoding and sample_rate_hertz for simplicity.
    audio_encoding = dialogflow2.enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
    sample_rate_hertz = 16000

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    with open(audioPath, 'rb') as audio_file:
        input_audio = audio_file.read()

    audio_config = dialogflow2.types.InputAudioConfig(
        audio_encoding=audio_encoding, language_code=language_code,
        sample_rate_hertz=sample_rate_hertz)
    query_input = dialogflow2.types.QueryInput(audio_config=audio_config)

    response = session_client.detect_intent(
        session=session, query_input=query_input,
        input_audio=input_audio)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))