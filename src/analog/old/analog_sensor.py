import spidev as sd
import time


# Object Class for Analog Sensor Reading via MCP3008
# - Provides various reading, conversion, and handling options.
# - Supports thread-based parallel logging on all channels via hardware lock.
class Analog_Sensor:

    # Global SPI Variable -- used by all sensor instances.
    spi = sd.SpiDev()
    spi.open(0,0)


    # Obj-specific variables
    # - Defines general operating parameters to be followed by the read methods.
    def __init__(self,channel,scalar=float(100/1023),offset=0,smoothing=None,lock=None,vref=3.3):
        if  channel > 7 or channel < 0:
            raise Exception('Channel value must be in range 0-7.')
        self.channel = channel  # Channel to be read from ADC -- Required Argument
        self.scalar = scalar  # 'slope' of conversion equation -- default is for % of total range
        self.offset = offset  # 'y-intercept' of conversion equation -- zero by default
        self.smoothing = smoothing  # Number of samples to avg per reading -- defaults to None (single-reading)
        self.lock = lock  # Hardware Lock for multithreading applications -- None by defualt
        self.vref = vref  # Reference voltage of ADC -- 3.3 by default


    # Object info query function.
    # - Returns dict of all current object-level variables.
    # - Useful for applying and/or troubleshooting cases of iterative object generation.
    def info(self):
        info = {'channel':self.channel,'scalar':self.scalar,'offset':self.offset,
                'smoothing':self.smoothing,'lock':self.lock,'vref':self.vref,'spi':self.spi}
        return info


    # Direct ADC bit reader.
    # - Core functionality of the class, all other methods read ADC via this function.
    # - Lock() support for threading based deployment.
    def get_bits(self):
        if self.lock: self.lock.acquire()  # Support for threading.Lock() method.
        adc = self.spi.xfer2([1,(8+self.channel)<<4,0])
        bits = ((adc[1]&3) << 8) + adc[2]
        if self.lock: self.lock.release()
        return bits


    # Average bit reader.
    # - Called internally when smoothing value is given.
    # - Takes average over n .2 second intervals (n=smoothing value).
    # - Not intended for direct call by client.
    def avg_bits(self):
        if not self.smoothing: raise Exception('Smoothing Value Not Provided.')  # r_pi edit:  Added exception for avg call w/o smoothing value
        bit_stack = []
        for s in range(self.smoothing):  # r_pi edit:  added 'self' to smoothing
            time.sleep(.2)
            bit_stack.append(self.get_bits())  # r_pi edit:  added 'self' to get_bits()
        smooth_bits = sum(bit_stack)/len(bit_stack)
        return smooth_bits


    # Voltage reading function.
    # - Converts bits to voltage based on current vref value.
    # - Function can optionally be passed a dict if {time:[reading]} output is needed.
    def get_volts(self,val_dict=None):
        if self.smoothing: bits = self.avg_bits()  # r_pi edit:  added 'self' to smoothing
        else: bits = self.get_bits()
        raw_volts = (bits * float(self.vref))/float(1023)
        volts = round(raw_volts,2)  # r_pi edit: changed 'volts' to 'raw_volts'
        if val_dict: val_dict[time.time()] = volts  # Appends time-keyed reading to dict if passed.
        return volts


    # Primary read function
    # - Returns a converted reading based on y = <scalar>*x + <offset> formula.
    # - Function can optionally be passed a dict if {time:[reading]} output is needed.
    def read(self,val_dict=None):
        if self.smoothing: bits = self.avg_bits()  # r_pi edit:  added 'self' to smoothing
        else: bits = self.get_bits()
        val = (bits * self.scalar) + self.offset
        if val_dict: val_dict[time.time()] = [val]  # Appends time-keyed reading to dict if passed.
        return val


    # Explicitly scheduled 'deployment' function.
    # - Accepts dict w/ unix-time keys for scheduling & value storage.
    # - If implimenting threading, sched_dict should not be shared asset.
    def scheduled_deployment(self,sched_dict,calibrate=False):
        if not calibrate: get_read = self.read
        elif self.smoothing: get_read = self.avg_bits
        else: get_read = self.get_bits
        start_time = time.time()
        run = sorted([x for x in sched_dict.keys() if x > start_time])
        while len(run) > 0:
            event = run.pop(0)
            delta = event - time.time()
            if delta > .2: time.sleep(delta)
            sched_dict[event] += [get_read()]
            print('Time: {0} Channel: {1} Reading: {2}'.format(round(event),
                                                               self.channel,
                                                               sched_dict[event]))

        return sched_dict

