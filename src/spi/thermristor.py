#!/usr/bin/env python3
from mcp3008 import mcp
import time
import json

# Execute a reading w/ thread lock.
def lkread(spi,ch,avg,lock):
    reading = 0.0
    for i in range(avg-1):
        with lock:
            reading += spi.read(ch)
        time.sleep(0.3)
    with lock:
        reading += spi.read(ch)
    return reading / avg

# Execute a reading w/o thread lock.
def nlread(spi,ch,avg):
    reading = 0.0
    for i in range(avg-1):
        reading += spi.read(ch)
        time.sleep(0.3)
    reading += spi.read(ch)
    return reading / avg

# Generate a log/reading at a specific time.
def mklog(spi,ch,time,avg,lock):
    delta = time - time.time()
    reading = 0.0
    if delta > 0.1: time.sleep(delta)
    if lock: return lkread(spi,ch,avg,lock)
    else: return nlread(spi,ch,avg)

# Master function -- orchestrates logging.
# Args: channel num, uxtime schedule, [average num], [threading lock]
# Returns a dict of form: {timestamp: value}
def log(ch,sched,avg=1,lock=None):
    with open('calibrations/thermristor.json') as fp:
        cal = json.load(fp)
    sched = sorted([s for s in sched if s > time.time()])
    with mcp() as spi:
        return {t: mklog(spi,ch,t,avg,lock) for t in sched}

