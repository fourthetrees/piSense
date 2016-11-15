#!/usr/bin/env python3
from ftplib import FTP

def push(fname,lpath,rpath,server,ident):
    # Filepath, Server IP, (username,password)
    cmd = 'STOR {}'.format(fname)
    with open(fname+lpath,'rb') as fp:
        with FTP(server,*ident) as con:
            con.cwd(rpath)
            con.storbinary(cmd,fp)

def Main():
    fname = 'ftp_test.txt'
    lpath = '/home/forrest/piSense/tmp/ftp/'
    rpath = '/'
    server = 'someIP'
    ident = ('username','password')
    try:
        push(fname,lpath,rpath,server,ident)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    Main()

