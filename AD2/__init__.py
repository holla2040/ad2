#!/usr/bin/env python

from ctypes import *
from dwfconstants import *

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

        self.dwf.FDwfAnalogIOChannelNodeSet(self.hdwf,c_int(0),c_int(0),c_double(True)) # enable positive supply
        self.dwf.FDwfAnalogIOChannelNodeSet(self.hdwf,c_int(1),c_int(0),c_double(True)) # enable negative supply
        self.dwf.FDwfAnalogIOEnableSet(self.hdwf,c_int(True))

    def open(self):
        self.dwf.FDwfDeviceOpen(c_int(-1),byref(self.hdwf)) # open the first ad2
        if self.hdwf.value == hdwfNone.value:
            print "failed to open device"
            quit()

    def close(self):
        self.dwf.FDwfDeviceClose(self.hdwf)

    @property
    def vpos(self):
        v = c_double()
        self.dwf.FDwfAnalogIOChannelNodeGet(self.hdwf,c_int(0),c_int(1),byref(v))
        return v.value

    @vpos.setter
    def vpos(self,value):
        self.dwf.FDwfAnalogIOChannelNodeSet(self.hdwf,c_int(0),c_int(1),c_double(value))

    @property
    def vneg(self):
        v = c_double()
        self.dwf.FDwfAnalogIOChannelNodeGet(self.hdwf,c_int(1),c_int(1),byref(v))
        return v.value

    @vneg.setter
    def vneg(self,value):
        self.dwf.FDwfAnalogIOChannelNodeSet(self.hdwf,c_int(1),c_int(1),c_double(value))
        

if __name__ == "__main__":
    ad = AD2()
    print "version",ad.dwfversion


