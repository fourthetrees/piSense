#!/usr/bin/env python3
import sqlite3 as sql
from os.path import expanduser
import time
from datatypes import Row

# Handles creation & interaction with db file of sensor readings.
# Readings divided into tables by sensor id.
# All data represented in form (datetime,value)

class sqlite_interface:

    def __init__(self,deployment='default',agent=None):
        # Parse database uri & generate required resources as necessary.
        self.tmp_directory = '~/piSense/tmp/' # Use user-agnostic ~/dir.
        self.database = expanduser(self.tmp_directory + '{0}.db'.format(str(deployment)))
        self.queries = {
                'push': 'INSERT INTO {0} (datetime, value) VALUES (?, ?)',
                'pull': 'SELECT * FROM {0}',
                'make': 'CREATE TABLE {0} (datetime REAL,value REAL, UNIQUE (datetime))',
                'look': 'SELECT name FROM sqlite_master WHERE type="table" AND name="{0}"',
                'tpull': 'SELECT name FROM sqlite_master WHERE type="table"'
        }
        if agent: self.set_table(agent)
        else: self.tableName = None

    def query(self,query,vals=None):
        # General query method; returns all outputs unmodified.
        try:
            with sql.connect(self.database) as con:
                if vals: q = con.execute(query,vals)
                else: q = con.execute(query)
                r = q.fetchall()
                return r
        except Exception as e:
            print(e)

    def push(self,reading):
        # Single row insertion; accepts a named tuple of form (datetime,vale).
        if not reading._fields == (' datetime','value'):
            raise TypeError('Input must be named tuple of form (datetime,value)')
        if not self.tableName: raise Exception('No Agent/Table name defined.')
        cmd = '''INSERT INTO {0} (datetime, value)
        VALUES (?, ?)'''.format(self.tableName)
        try:
            with sql.connect(self.database) as con:
                con.execute(cmd,reading)
        except Exception as e:
            print(e)

    def pull(self,rangetuple=None): # range should be unix time tuple of form (start,stop).
        # Query a range of times from db file.  Defaults to past 24 hours if no arg given.
        if not rangetuple:
            rangetuple = (time.time()-86400,time.time())
        cmd = 'SELECT * FROM {0} WHERE datetime BETWEEN ? AND ?'.format(self.tableName)
        return self.query(cmd,vals=rangetuple)

    def dump(self,readings):
        # Bulk insertion; accepts a list of named tuples of form (datetime,value).
        if not readings[0]._fields == ('datetime','value'):
            raise TypeError('Input must be named tuple of form (datetime,value)')
        if not self.tableName: raise Exception('No Agent/Table name defined.')
        cmd = '''INSERT INTO {0} (datetime, value)
        VALUES (?, ?)'''.format(self.tableName)
        with sql.connect(self.database) as con:
            for row in readings:
                try:
                    con.execute(cmd,row)
                    con.commit()
                except Exception as e:
                    if not 'UNIQUE' in str(e): print(e)

    def build_table(self):
        # Create table. Called by agnostic.
        cmd = '''CREATE TABLE {0}
        (datetime REAL,value REAL, UNIQUE (datetime))'''.format(self.tableName)
        try:
            with sql.connect(self.database) as con:
                con.execute(cmd)
        except Exception as e:
            print(e)

    def set_table(self,tableName):
        # Set current table name, check if table exists, and call build if necessary.
        self.tableName = tableName
        q = 'SELECT name FROM sqlite_master WHERE type="table" AND name="{0}"'
        r = self.query(q.format(self.tableName))
        if not r: self.build_table()


    def dump_many(self,reading_dict):
        # Execute dumpts to multiple tables; accepts dict of form {sensor_id:[readings]}.
        for sensor in reading_dict:
            readings = reading_dict[sensor]
            if readings:
                self.set_table(sensor)
                self.dump(readings)

    def check_archive(self):
        # Check for existence of archive table & generate if necessary.
        cmd = 'SELECT name FROM sqlite_master WHERE type="table" AND name="archive"'
        if self.query(cmd): return
        # Make archive table w/ UNIQUE of sensor_id/datetime pair.
        cmd = '''CREATE TABLE archive
        (sensor_id TEXT, datetime REAL, value REAL, UNIQUE (sensor_id, datetime))'''
        try:
            with sql.connect(self.database) as con:
                con.execute(cmd)
        except Exception as e:
            print(e)

    def archive(self):
        self.check_archive()
        data = self.pull_all()
        for sn in data:
            print(sn)
            # Merge table
        return data

    def arch_pull(self):
        with sql.connect(self.database) as con:
            cur = con.execute(self.queries['tpull'])
            tables = [x[0] for x in cur.fetchall()]
            data = {}
            for sensor_id in tables:
                cmd = self.queries['pull'].format(sensor_id)
                cur.execute(cmd)
                rows = [Row(sensor_id=sensor_id,datetime=float(x[0]),
                             value=float(x[1])) for x in cur.fetchall()]
                data[sensor_id] = rows
        return data
