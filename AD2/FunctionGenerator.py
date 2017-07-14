#!/usr/bin/env python

from ctypes import *
from dwfconstants import *

import time,sys

class FunctionGenerator(object):
    def __init__(self,dwf,hdwf,channel):
        self.dwf = dwf
        self.hdwf = hdwf
        self.channel = c_int(channel)

        self.dwf.FDwfAnalogOutNodeEnableSet(self.hdwf, self.channel, AnalogOutNodeCarrier, c_bool(True))
        self.dwf.FDwfAnalogOutNodeFunctionSet(self.hdwf, self.channel, AnalogOutNodeCarrier, funcSine)
        self.frequency = 0.00
        self.amplitude = 0.00
        self.offset    = 0.00

        self.configure()

    def configure(self):
        self.dwf.FDwfAnalogOutConfigure(self.hdwf, self.channel, c_bool(True))

    @property
    def frequency(self):
        v = c_double()
        self.dwf.FDwfAnalogOutNodeFrequencyGet(self.hdwf, self.channel, AnalogOutNodeCarrier, byref(v))
        return v.value

    @frequency.setter
    def frequency(self,value):
        self.dwf.FDwfAnalogOutNodeFrequencySet(self.hdwf, self.channel, AnalogOutNodeCarrier, c_double(value))
        self.configure()

    @property
    def amplitude(self):
        v = c_double()
        self.dwf.FDwfAnalogOutNodeAmplitudeGet(self.hdwf,self.channel,AnalogOutNodeCarrier,byref(v))
        return v.value

    @amplitude.setter
    def amplitude(self,value):
        self.dwf.FDwfAnalogOutNodeAmplitudeSet(self.hdwf,self.channel,AnalogOutNodeCarrier,c_double(value))
        self.configure()

    @property
    def offset(self):
        v = c_double()
        self.dwf.FDwfAnalogOutNodeOffsetGet(self.hdwf,self.channel,AnalogOutNodeCarrier,byref(v))
        return v.value

    @offset.setter
    def offset(self,value):
        self.dwf.FDwfAnalogOutNodeOffsetSet(self.hdwf,self.channel,AnalogOutNodeCarrier,c_double(value))
        self.configure()


