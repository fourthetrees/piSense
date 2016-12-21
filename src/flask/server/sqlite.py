#!/usr/bin/env python3
import sqlite3 as sql
from flask import g

def get_db(dbname):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect(dbname)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


