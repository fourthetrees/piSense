## Usage: sqlite

The `push()` function auto-generates database and tables as needed.  Args are database name and a dictionary of sensor readings in the form `{sensor: [(timestamp,value), ...]}`.  The `pull()` function returns a dictionary of all stored readings and requires database name as arg.
```
>>> import sqlite as sql
>>> db = 'thisdb'
>>> data = {
...    'sensor001': [(timestamp, value), ...],
...    'sensor002': [(timestamp, value), ...]
...}
>>> sql.push(db,data)
>>> sql.pull(db)
  {'sensor001': [(timestamp, value), ...],
  'sensor002': [(timestamp, value), ...]}
```

**Future Work:** Generate a thread safe method of 'archiving' values which have been successfully uploaded.
