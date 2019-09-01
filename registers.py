import sys
import os
import time

import flask
import requests
import MySQLdb
import bd

blueprint = flask.Blueprint('registers', __name__)

@blueprint.route('/registers', methods=[ 'GET' ])
def SelectReq():
    context = {
        'title': 'Hacka | Pepe',
        'requisicoes': bd.RequisicoesDeCadastros.query.all()
    }
    return flask.render_template('registers.html', context=context)