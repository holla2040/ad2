#!/usr/bin/env python

from ctypes import *
from dwfconstants import *

class Trigger(object):
    def __init__(self,dwf,hdwf):
        self.dwf = dwf
        self.hdwf = hdwf

    @property
    def autotimeout(self):
        v = c_double()
        self.dwf.FDwfAnalogInTriggerAutoTimeoutGet(self.hdwf,byref(v))
        return v.value 
    @autotimeout.setter
    def autotimeout(self,value):
        self.dwf.FDwfAnalogInTriggerAutoTimeoutSet(self.hdwf,c_double(value))

    @property #see TRIGSRC
    def source(self):
        v = c_ubyte()
        self.dwf.FDwfAnalogInTriggerSourceGet(self.hdwf,byref(v))
        return v 
    @source.setter
    def source(self,value):
        self.dwf.FDwfAnalogInTriggerSourceSet(self.hdwf,value)

    @property #see TRIGTYPE
    def type(self):
        v = c_ubyte()
        self.dwf.FDwfAnalogInTriggerTypeGet(self.hdwf,byref(v))
        return v 
    @type.setter
    def type(self,value):
        self.dwf.FDwfAnalogInTriggerTypeSet(self.hdwf,value)

    @property 
    def channel(self):
        v = c_int()
        self.dwf.FDwfAnalogInTriggerChannelGet(self.hdwf,byref(v))
        return v.value
    @channel.setter
    def channel(self,value):
        self.dwf.FDwfAnalogInTriggerChannelSet(self.hdwf,c_int(value))

    @property
    def level(self):
        v = c_double()
        self.dwf.FDwfAnalogInTriggerLevelGet(self.hdwf,byref(v))
        return v.value 
    @level.setter
    def level(self,value):
        self.dwf.FDwfAnalogInTriggerLevelSet(self.hdwf,c_double(value))

    @property #FILTER
    def filter(self):
        v = c_int()
        self.dwf.FDwfAnalogInTriggerFilterGet(self.hdwf,byref(v))
        return v
    @filter.setter
    def filter(self,value):
        self.dwf.FDwfAnalogInTriggerFilterSet(self.hdwf,value)

    @property #TRIGCOND
    def condition(self):
        v = c_int()
        self.dwf.FDwfAnalogInTriggerConditionGet(self.hdwf,byref(v))
        return v
    @condition.setter
    def condition(self,value):
        self.dwf.FDwfAnalogInTriggerConditionSet(self.hdwf,value)

