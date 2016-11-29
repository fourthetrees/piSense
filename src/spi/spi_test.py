#!/usr/bin/env python3
from spi import spi
import time

def read_adc():
    with spi() as sc:
        ch0,ch7 = sc.read(0),sc.read(7)
    return ch0,ch7

def Main():
    while True:
        i = input('Read ADC? (y/n)')
        if 'n' in i: return
        ch0,ch7 = read_adc()
        print('Ch_0: {} Ch_7: {}'.format(ch0,ch7))

if __name__ == '__main__':
    Main()
