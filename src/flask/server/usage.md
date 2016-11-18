### Basic Server Usage

#### Setup:
```
$ export FLASK_APP=main.py
$ flask run
```

#### Interaction:

**Uplaoding Sensor Data:** HTTP POST of json data to `http://somehost/raspi/<deployment>`

**Downloading Deployment Data:** HTTP GET to `http://somehost/raspi/<deployment>`

