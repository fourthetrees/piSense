#!/usr/bin/env python3

from sqlite_interface import sqlite_interface
from datatypes import Reading

sql = sqlite_interface(deployment='test001')

l1 = [Reading(12,13), Reading(18,19), Reading(20,21)]
l2 = [Reading(1,4), Reading(113,144), Reading(99,11)]

d = {
        'tt001': l1,
        'tt002': l2
}

sql.dump_many(d)
data = sql.arch_pull()
print(data)

