#!/usr/bin/env python3
from os.path import expanduser
from sys import argv
from ftplib import FTP

# Simple FTP command line script.
# Accepts 1 arg: filename

# Unencrypted; do not use privileged login.
server = 'hostname'
username = 'uname'
password = 'pass'

remote_path = '~/'
local_path = '~/Downloads/'

# FTP() understands ~/ notation; open() does not.
file = expanduser(local_path + argv[1])

# Nested context managers; very wow!
with open(file, 'rb') as fp:
    with FTP(server, username, password) as conn:
        # Navigate & write to file.
        conn.cwd(remote_path)
        conn.storbinary(file,fp)

# Confirmation.
print('process complete.')