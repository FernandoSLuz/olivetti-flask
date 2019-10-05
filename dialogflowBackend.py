import sys
import os
import time
import json

import flask
from flask import request
import requests as req
from flask import Blueprint
import bd

blueprint = flask.Blueprint('dialogflowBackend', __name__)

def checkNumberStatus():
    print("status")
    #here we will check if number exists on our database, and as well if it is in an existing conversation
    #if user is not on a conversation, create a new conversation id
    #if user in a conversation, get it's id
    #send user message to dialogflow