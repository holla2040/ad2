#!/usr/bin/env python

from ctypes import *
from dwfconstants import *
import PowerSupply,FunctionGenerator,Trigger,Oscilloscope

import time,sys

class AD2(object):
    def __init__(self):
        if sys.platform.startswith("win"):
            self.dwf = cdll.dwf
        elif sys.platform.startswith("darwin"):
            self.dwf = cdll.LoadLibrary("/Library/Frameworks/dwf.framework/dwf")
        elif sys.platform.startswith("cygwin"):
            self.dwf = CDLL("dwf.dll")
        else:
            self.dwf = cdll.LoadLibrary("libdwf.so")

        self.hdwf = c_int()

        v = create_string_buffer(16)
        self.dwf.FDwfGetVersion(v)
        self.dwfversion = v.value

        self.open() 

        self._vposSetOffset = 0.0
        self._vposGetOffset = 0.0

        self.vpos = PowerSupply.PowerSupply(self.dwf,self.hdwf,0)
        self.vneg = PowerSupply.PowerSupply(self.dwf,self.hdwf,1)

        self.fg1 = FunctionGenerator.FunctionGenerator(self.dwf,self.hdwf,0)
        self.fg2 = FunctionGenerator.FunctionGenerator(self.dwf,self.hdwf,1)

        self.dwf.FDwfAnalogIOEnableSet(self.hdwf,c_int(True))

        self.scope   = Oscilloscope.Oscilloscope(self.dwf,self.hdwf)

    def open(self):
        self.dwf.FDwfDeviceOpen(c_int(-1),byref(self.hdwf)) # open the first ad2
        if self.hdwf.value == hdwfNone.value:
            print "failed to open device"
            quit()

    def close(self):
        self.dwf.FDwfDeviceClose(self.hdwf)

if __name__ == "__main__":
    ad = AD2()
    print "version",ad.dwfversion
