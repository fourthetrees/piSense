### Basic Server Usage

#### Setup:
Basic:
```
$ export FLASK_APP=main.py
$ flask run
```
Some linux distros don't play nicely with flask's encoding by default.  If flask complains try running:
```
$ export LC_ALL=C.UTF-8
$ export LANG=C.UTF-8
```

#### Interaction:

**Uplaoding Sensor Data:** HTTP POST of json data to `http://somehost/raspi/<deployment>`

**Downloading Deployment Data:** HTTP GET to `http://somehost/raspi/<deployment>`

