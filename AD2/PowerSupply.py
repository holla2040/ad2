#!/usr/bin/env python

from ctypes import *
from dwfconstants import *

class PowerSupply(object):
    def __init__(self,dwf,hdwf,channel):
        self.dwf = dwf
        self.hdwf = hdwf
        self.channel = c_int(channel)

        self._setOffset = 0.0
        self._getOffset = 0.0

        self.dwf.FDwfAnalogIOChannelNodeSet(self.hdwf,self.channel,c_int(0),c_double(True)) # enable supply

    @property
    def voltage(self):
        v = c_double()
        self.dwf.FDwfAnalogIOChannelNodeGet(self.hdwf,self.channel,c_int(1),byref(v))
        return v.value + self._getOffset
    @voltage.setter
    def voltage(self,value):
        self.dwf.FDwfAnalogIOChannelNodeSet(self.hdwf,self.channel,c_int(1),c_double(value+self._setOffset))

    @property
    def setOffset(self):
        return self._setOffset
    @setOffset.setter
    def setOffset(self,value):
        self._setOffset = value

    @property
    def getOffset(self):
        return self._getOffset
    @getOffset.setter
    def getOffset(self,value):
        self._getOffset = value

