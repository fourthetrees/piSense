#!/usr/bin/env python3
from spi import spi
import time

def read_adc():
    with spi() as sc:
        data = sc.read()
    return data

def Main():
    while True:
        i = input('Read ADC? (y/n)')
        if 'n' in i: return
        print(read_adc())

if __name__ == '__main__':
    Main()
