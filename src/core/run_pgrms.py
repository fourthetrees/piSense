#!/usr/bin/env python3
from threading import Thread
import os

# Fork & replace child w/ target program.
# Returns PID of child process to parent.
def launch(pgrm,args):
    pid = os.fork()
    if not pid: os.execv(pgrm,[pgrm,*args])
    return pid


# Run & restart target up to `errmax` times.
# Returns number of restarts upon success.
# Raises exception if `errmax`value is exceeded.
def run(pgrm,args,errmax):
    for errcount in range(errmax):
        pid = launch(pgrm,args)
        _,code = os.waitpid(pid,0)
        if not code: return errcount
    raise Exception('errcount exceeded for {}'.format(pgrm))


# Spin up programs & monitors.
# Accepts dict of form: {program:[args],...}
# This is the intended entry-point for this workflow.
def spinup(programs,errmax=4):
    for p in programs:
        Thread(target=run,args=(p,programs[p],errmax)).start()
