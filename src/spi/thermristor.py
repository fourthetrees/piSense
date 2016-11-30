#!/usr/bin/env python3
from mcp3008 import mcp
import time
import json


def mklog(spi,channel,time,lock):
    

def log(channel,schedule,lock=None):
    with open('calibrations/thermristor.json') as fp:
        cal = json.load(fp)
    with mcp() as spi:

