#!/usr/bin/env python3
import spidev

# Context manager for reading from mcp3008 over SPI.
# Thread-Safe so long as read is passed an appropriate lock.
class mcp:

    # Returns a connection object.
    def __enter__(self,bus=0,device=0):
        self.spi = spidev.SpiDev()
        self.spi.open(bus,device)
        return self

    # Thread-safe read method (if lock is supplied).
    def read(self,channel,lock=None):
        if lock: lock.acquire()
        adc = self.spi.xfer2([1,(8+channel)<<4,0])
        bits = ((adc[1]&3) << 8) + adc[2]
        if lock: lock.release()
        return bits

    # Clean up connection on exit.
    def __exit__(self,*args):
        self.spi.close()

