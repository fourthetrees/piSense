#!/usr/bin/env python3
from flask import Flask
from flask import request
from flask import Response
import json

app = Flask(__name__)

# Generic greeting page
@app.route('/')
def landing():
    return 'hello world'

# Deployment post/get page for raspi
@app.route('/raspi/<deployment>', methods = ['GET','POST'])
def raspi(deployment):
    if request.method == 'POST':
        j = request.get_json(force=True)
        store_readings(deployment,j)
        return 'posted to {}'.format(deployment)
    else:
        data = get_deployment(deployment)
        rsp = Response(response=data, status=200,
                mimetype='application/json')
        return rsp

# Placeholder storage function
def store_readings(deployment,data):
    filename = '{}.json'.format(deployment)
    with open(filename,'w') as fp:
        json.dump(data,fp)

# Placeholder deployment update function
def get_deployment(deployment):
    filename = '{}.json'.format(deployment)
    with open(filename,'r') as fp:
        data = fp.read()
    return data

