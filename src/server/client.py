#!/usr/bin/env python3
import requests

# Post dict/json to uri.
def post(uri,data):
    p = requests.post(uri,json=data)
    if p.status_code != 200:
        raise Exception('http post failed.')

# Get dict/json from uri.
def get(uri):
    g = requests.get(uri)
    if g.status_code != 200:
        raise Exception('http get failed.')
    return g.json()

