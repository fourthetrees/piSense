#!/usr/bin/env python3
import spidev

class spi:

    def __enter__(self,bus=0,device=0):
        self.spi = spidev.SpiDev()
        self.spi.open(bus,device)
        return self

    def read(self,channel,lock=None):
        if lock: lock.acquire()
        adc = self.spi.xfer2([1,(8+channel)<<4,0])
        bits = ((adc[1]&3) << 8) + adc[2]
        if lock: lock.release()
        return bits

    def __exit__(self,*args):
        self.spi.close()
