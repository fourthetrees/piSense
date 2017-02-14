#!/usr/bin/env python3
import json

def get_deployment():
    with open('tmp/deployment.json') as fp:
        deployment = json.load(fp)
    return deployment

def get_identity():
    with open('tmp/identity.json') as fp:
        identity = json.load(fp)
    return identity

