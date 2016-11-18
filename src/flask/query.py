#!/usr/bin/env python3
import requests

uri = 'http://127.0.0.1:5000/raspi/test_deployment'
data = { # Note: http does not support nested dicts!
    'sensor001': [
        ('datetime', 'value'),
        ('apple', 99.99),
        ('antelope',0.002)
    ],
    'b': [
        ('bananna', 0.568),
        ('boron', 9.234),
        ('birch', 123.1)
    ],
    'd': {
        'k':'val',
        'k2':'val2'
    }
}

post = requests.post(uri,json=data)
get = requests.get(uri)

print('POST.......{}'.format(post.text))
print('GET:\n{}'.format(get.json()))
