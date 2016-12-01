#!/usr/bin/env python3
from mcp3008 import mcp
import time
import json

# Logging script for thermristors connected to the MCP3008.
# Calibration saved in file: (__file__)/calibration/thermristor.json
# Get a reading.
def read_val(spi,ch,avg,lock):
    reading = 0.0
    for i in range(avg-1):
        reading += spi.read(ch,lock=lock)
        time.sleep(0.3)
    reading += spi.read(ch,lock=lock)
    return round(reading/avg,2)

# Execute a log/reading at a specific time.
def mklog(spi,ch,t,avg,lock):
    delta = t - time.time()
    reading = 0.0
    if delta > 0.1: time.sleep(delta)
    return read_val(spi,ch,avg,lock)
    #if lock: return lkread(spi,ch,avg,lock)
    #else: return nlread(spi,ch,avg)

# Master function -- orchestrates logging.
# Args: channel num, uxtime schedule, [average num], [threading lock]
# Returns a dict of form: {timestamp: value}
def log(ch,sched,avg=1,lock=None):
    with open('calibration/thermristor.json') as fp:
        cal = json.load(fp)
    fmt = lambda x: x * cal['scalar'] + cal['offset']
    sched = sorted([s for s in sched if s > time.time()])
    with mcp() as spi:
        return {int(t): fmt(mklog(spi,ch,t,avg,lock)) for t in sched}

