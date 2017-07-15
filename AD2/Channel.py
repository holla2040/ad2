#!/usr/bin/env python

from ctypes import *
from dwfconstants import *
import numpy as np

import time,sys

class Channel(object):
    def __init__(self,dwf,hdwf,channel):
        self.dwf = dwf
        self.hdwf = hdwf
        self.channel = c_int(channel)

        self.dwf.FDwfAnalogInChannelEnableSet(self.hdwf,self.channel,c_bool(True))
        self.range = 5.0

    @property #FILTER
    def filter(self):
        v = c_int()
        self.dwf.FDwfAnalogInChannelFilterGet(self.hdwf,byref(v))
        return v
    @filter.setter
    def filter(self,value):
        self.dwf.FDwfAnalogInChannelFilterSet(self.hdwf,value)

    @property
    def range(self):
        v = c_double()
        self.dwf.FDwfAnalogInChannelRangeGet(self.hdwf,self.channel,byref(v))
        return v.value
    @range.setter
    def range(self,value):
        self.dwf.FDwfAnalogInChannelRangeSet(self.hdwf,self.channel,c_double(value))
    @property
    def rangeinfo(self):
        min = c_double()
        max = c_double()
        steps = c_int()
        self.dwf.FDwfAnalogInChannelRangeInfo(self.hdwf,byref(min),byref(max),byref(steps))
        return {'min':min.value,'max':max.value,'steps':steps.value}
    @property
    def rangesteps(self):
        rangesteps = (c_double*32)()
        steps = c_int()
        self.dwf.FDwfAnalogInChannelRangeSteps(self.hdwf,byref(rangesteps),byref(steps))
        return {'rangesteps':np.frombuffer(rangesteps),'steps':steps.value}

    @property #see FUNC
    def function(self):
        v = c_ubyte()
        self.dwf.FDwfAnalogOutNodeFunctionGet(self.hdwf,self.channel,AnalogOutNodeCarrier,byref(v))
        return v
    @function.setter
    def function(self,value):
        self.dwf.FDwfAnalogOutNodeFunctionSet(self.hdwf,self.channel,AnalogOutNodeCarrier,value)
        self.configure()

    @property
    def offset(self):
        v = c_double()
        self.dwf.FDwfAnalogInChannelOffsetGet(self.hdwf,self.channel,byref(v))
        return v.value
    @offset.setter
    def offset(self,value):
        self.dwf.FDwfAnalogInChannelOffsetSet(self.hdwf,self.channel,c_double(value))

    @property
    def attenuation(self):
        v = c_double()
        self.dwf.FDwfAnalogInChannelAttenuationGet(self.hdwf,self.channel,byref(v))
        return v.value
    @attenuation.setter
    def attenuation(self,value):
        self.dwf.FDwfAnalogInChannelAttenuationSet(self.hdwf,self.channel,c_double(value))
