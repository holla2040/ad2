#!/usr/bin/env python

from ctypes import *
from dwfconstants import *

import time,sys

class PowerSupply(object):
    def __init__(self,dwf,hdwf,channel):
        self.dwf = dwf
        self.hdwf = hdwf
        self.channel = channel

        self._setOffset = 0.0
        self._getOffset = 0.0

        self.dwf.FDwfAnalogIOChannelNodeSet(self.hdwf,c_int(self.channel),c_int(0),c_double(True)) # enable positive supply

    @property
    def voltage(self):
        v = c_double()
        self.dwf.FDwfAnalogIOChannelNodeGet(self.hdwf,c_int(self.channel),c_int(1),byref(v))
        return v.value + self._getOffset

    @voltage.setter
    def voltage(self,value):
        self.dwf.FDwfAnalogIOChannelNodeSet(self.hdwf,c_int(self.channel),c_int(1),c_double(value+self._setOffset))

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

