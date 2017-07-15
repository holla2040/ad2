#!/usr/bin/env python

from ctypes import *
from dwfconstants import *
import numpy as np
import sys,time
import Trigger,Channel

class Oscilloscope(object):
    def __init__(self,dwf,hdwf):
        self.dwf = dwf
        self.hdwf = hdwf
    
        self.ch1 = Channel.Channel(self.dwf,self.hdwf,0)
        self.ch2 = Channel.Channel(self.dwf,self.hdwf,1)

        self.frequency  = 100000.00
        self.buffersize = 512
        self.trigger = Trigger.Trigger(self.dwf,self.hdwf)

    def reset(self):
        self.dwf.FDwfAnalogInReset(self.hdwf)

    def run(self):
        self.dwf.FDwfAnalogInConfigure(self.hdwf,c_bool(True),c_bool(True))

    def stop(self):
        self.dwf.FDwfAnalogInConfigure(self.hdwf,c_bool(True),c_bool(False))

    def single(self):
        self.dwf.FDwfAnalogInAcquisitionModeSet(self.hdwf,acqmodeSingle)
        # self.trigger.autotimeout = 0
        self.dwf.FDwfAnalogInConfigure(self.hdwf,c_bool(False),c_bool(True))

    def triggered(self): # tba
        return True

    def dataready(self): # tba
        return True
    
    def read(self): # blocking
        bufsize = c_int()
        status = c_byte()
        self.dwf.FDwfAnalogInBufferSizeGet(self.hdwf,byref(bufsize))
        bufsize = bufsize.value
        ch1samples = (c_double*bufsize)()
        ch2samples = (c_double*bufsize)()
        while True:
            self.dwf.FDwfAnalogInStatus(self.hdwf, c_int(1), byref(status))
            if status.value == DwfStateDone.value:
                break
            time.sleep(0.001)
        self.dwf.FDwfAnalogInStatusData(self.hdwf,0,ch1samples,bufsize)
        self.dwf.FDwfAnalogInStatusData(self.hdwf,1,ch2samples,bufsize)
        return (np.array(ch1samples),np.array(ch2samples))


    @property
    def buffersize(self):
        v = c_int()
        self.dwf.FDwfAnalogInBufferSizeGet(self.hdwf,byref(v))
        return v.value
    @buffersize.setter
    def buffersize(self,value):
        min = c_int()
        max = c_int()
        self.dwf.FDwfAnalogInBufferSizeInfo(self.hdwf,byref(min),byref(max))
        min = min.value
        max = max.value
        if value < min:
            value = min
        if value > max:
            value = max
        self.dwf.FDwfAnalogInBufferSizeSet(self.hdwf,c_int(value))

    @property
    def frequency(self):
        v = c_double()
        self.dwf.FDwfAnalogInFrequencyGet(self.hdwf,byref(v))
        return v.value
    @frequency.setter
    def frequency(self,value):
        self.dwf.FDwfAnalogInFrequencySet(self.hdwf,c_double(value))
