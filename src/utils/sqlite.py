#!/usr/bin/env python3
import sqlite3 as sql

# Execute an sql command.
def execute(db,query,data=None):
    with sql.connect('{}.db'.format(db)) as con:
        if data: q = con.executemany(query,data)
        else: q = con.execute(query)
        return q.fetchall()

# Generate table.
def mktable(db,table):
    cmd = 'CREATE TABLE {} (datetime REAL, value REAL, UNIQUE (datetime))'
    execute(db,cmd.format(table))

# Return list of tables.
def tables(db):
    cmd = 'SELECT name FROM sqlite_master WHERE type="table"'
    return [t[0] for t in execute(db,cmd)]

# Uplaod dictionary of readings.
def push(db,data):
    cmd = 'INSERT INTO {} (datetime, value) VALUES (?, ?)'
    tbl = tables(db)
    for sn in data:
        if not sn in tbl: mktable(db,sn)
        execute(db,cmd.format(sn),data=data[sn])

# Get all values.
def pull(db):
    cmd = 'SELECT * FROM {}'
    data = {}
    for t in tables(db):
        data[t] = execute(db,cmd.format(t))
    return data

