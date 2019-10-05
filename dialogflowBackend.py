import sys
import os
import time
import json

import flask
from flask import request
import requests as req
from flask import Blueprint


blueprint = flask.Blueprint('dialogflowBackend', __name__)


def newMessage(phone, message):
    print(phone)
    print(message)

def checkNumberStatus():
    print("status")
    #here we will check if number exists on our database, and as well if it is in an existing conversation
    #if user is not on a conversation, create a new conversation id
    #if user in a conversation, get it's id
    #send user message to dialogflow

@blueprint.route('/testintents', methods=[ 'POST'])
def testintents():
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    print("hello")
    #detect_intent_texts("chatbot-olivetti", str(form['sessionId']), str(form['message']), str(form['languageCode']))


def detect_intent_texts(project_id, session_id, text, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))