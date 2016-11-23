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

# Example Usage
def Main():
    import json
    eg_file = 'example.json'
    uri = 'http://127.0.0.1:5000/raspi/test_deployment'
    with open(eg_file) as fp:
        data = json.load(fp)
    post(uri,data)
    print(get(uri))

if __name__ == '__main__':
    Main()

