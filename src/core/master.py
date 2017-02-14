#!/usr/bin/env python3
from src.core.params import get_identity,get_deployment
from src.core.programs import spinup
from src.server.client import get, post
from src.utils.sched import schedule
from src.utils.sqlite import pull
import time

def get_params():
    identity = get_identity()
    try:
        deployment = get_deployment()
    except:
        deployment = get(ident['portal'] + ident['ident'])
    return identity,deployment


def launch_programs(deployment):
    programs = deployment['programs']
    for p in programs if not 'start' in p:
        p['start'] = deployment['start']
    spinup(programs)


def sheduled_upload(identity,deplyoment):
    now = lambda: time.time()
    wait = lambda t: time.sleep(t - time.time())
    start,interval = deployment['start'],deployment['interval']
    usched = schedule(start+interval,interval)
    for timeindex in sched if timeindex > now():
        time.sleep(delta())




def run():
    identity,deployment = get_params()
    launch_programs(deployment)


