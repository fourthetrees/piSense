### Ras_Pi Analog Sensor Class

import spidev as sd
import time

class Analog_Sensor:  # Generate Sensor Objects for Reading.

    spi = sd.SpiDev()  # Global SPI Variable -- used by all sensor instances.
    spi.open(0,0)
    
    def __init__(self,channel,scalar=None,smoothing=None,lock=None,vref=3.3):  # Sensor-Specific Variables.
        if  channel > 7 or channel < 0:
            raise Exception('Channel value must be in range 0-7.')
        self.channel = channel
        self.scalar = scalar
        self.smoothing = smoothing
        self.lock = lock
        self.vref = vref
    
    def info(self):  # Return Dict of all important properties w/ var names as keys.
        info = {'channel':self.channel,'scalar':self.scalar,'smoothing':self.smoothing,
                'lock':self.lock,'vref':self.vref,'spi':self.spi}
        return info
    
    def get_bits(self):  # Get raw bits from ADC.
        if self.lock: self.lock.acquire()  # Support for threading.Lock() method.
        adc = self.spi.xfer2([1,(8+self.channel)<<4,0])
        bits = ((adc[1]&3) << 8) + adc[2]
        if self.lock: self.lock.release()
        return bits

    def avg_bits(self):  # Take the avg of n readings across .2*n seconds.  
        bit_stack = []
        for s in range(smoothing):
            time.sleep(.2)
            bit_stack.append(get_bits())
        smooth_bits = sum(bit_stack)/len(bit_stack)
        return smooth_bits

    def get_volts(self):  # Get bits and convert to Voltage reading.
        if smoothing: bits = self.avg_bits()
        else: bits = self.get_bits()
        raw_volts = (bits * float(self.vref))/float(1023)
        volts = round(volts,2)
        return volts
    
    def read(self):  # Read Sensor.  Returns percent value if no scalar given.
        if smoothing: bits = self.avg_bits()
        else: bits = self.get_bits()
        if not self.scalar: self.scalar = float(100/1023)
        val = bits * self.scalar
        return val
