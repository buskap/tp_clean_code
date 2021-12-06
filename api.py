from flask import Flask, jsonify
import flask
from flask.globals import request
import functions
from functions.functions import keyVerification
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True 

@app.route('/', methods=['GET'])
def home():
    return jsonify({
                'status': 'ok',
                'request': "A123456789",
                'result': 1,
            })
@app.route('/client/cle/verification/', methods=['GET'])
def verif():
    id = request.args.get('id', None)
    if(keyVerification(id) == True):
        return jsonify({
            'status': 'ok',
            'request': id,
            'result': 1,
        })
    else:
        return jsonify({
            'status': 'ok',
            'request': id,
            'result': 0,
        })

app.run()
