#!/usr/bin/env python3

from collections import namedtuple

Reading = namedtuple('reading',['datetime','value'])

Row = namedtuple('row',['sensor_id','datetime','value'])
