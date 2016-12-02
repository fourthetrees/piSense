#!/usr/bin/env python3

def schedule(state,interval):
    yield state
    while True:
        state += interval
        yield state

