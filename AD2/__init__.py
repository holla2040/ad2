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

        self._vposSetOffset = 0.0
        self._vposGetOffset = 0.0
        self._vnegSetOffset = 0.0
        self._vnegSetOffset = 0.0

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
        return v.value + self._vposGetOffset

    @vpos.setter
    def vpos(self,value):
        self.dwf.FDwfAnalogIOChannelNodeSet(self.hdwf,c_int(0),c_int(1),c_double(value+self._vposSetOffset))

    @property
    def vposSetOffset(self):
        return self._vposSetOffset

    @vposSetOffset.setter
    def vposSetOffset(self,value):
        self._vposSetOffset = value

    @property
    def vposGetOffset(self):
        return self._vposGetOffset

    @vposGetOffset.setter
    def vposGetOffset(self,value):
        self._vposGetOffset = value









    @property
    def vneg(self):
        v = c_double()
        self.dwf.FDwfAnalogIOChannelNodeGet(self.hdwf,c_int(1),c_int(1),byref(v))
        return v.value + self._vnegGetOffset

    @vneg.setter
    def vneg(self,value):
        self.dwf.FDwfAnalogIOChannelNodeSet(self.hdwf,c_int(1),c_int(1),c_double(value+self._vnegSetOffset))

    @property
    def vnegSetOffset(self):
        return self._vnegSetOffset

    @vnegSetOffset.setter
    def vnegSetOffset(self,value):
        self._vnegSetOffset = value

    @property
    def vnegGetOffset(self):
        return self._vnegGetOffset

    @vnegGetOffset.setter
    def vnegGetOffset(self,value):
        self._vnegGetOffset = value

        

if __name__ == "__main__":
    ad = AD2()
    print "version",ad.dwfversion
