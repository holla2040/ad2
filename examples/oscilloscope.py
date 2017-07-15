#!/usr/bin/env python

import sys,time
sys.path.append('..')
import AD2
from AD2.dwfconstants import *


d = AD2.AD2()

print "buffersize"
print d.scope.buffersize
d.scope.buffersize = 4000000
print d.scope.buffersize
d.scope.buffersize = 512
print d.scope.buffersize

print "\nrange"
print d.scope.ch1.rangeinfo
print d.scope.ch1.range
d.scope.ch1.range = 10.0
print d.scope.ch1.range

print "\noffset"
print d.scope.ch1.offset
d.scope.ch1.offset = 10.0
print d.scope.ch1.offset

print "\nattenuation"
print d.scope.ch1.attenuation
d.scope.ch1.attenuation = 100.0
print d.scope.ch1.attenuation
d.scope.ch1.attenuation = 10.0
print d.scope.ch1.attenuation
d.scope.ch1.attenuation = 1.0
print d.scope.ch1.attenuation



d.scope.reset()
d.scope.buffersize          = 1000
d.scope.frequency           = 1000000
d.scope.trigger.type        = trigtypeEdge
d.scope.trigger.channel     = 0
d.scope.trigger.level       = 1.5
d.scope.trigger.condition   = trigcondRisingPositive
time.sleep(2)
d.scope.single()
data = d.scope.read()
# print data

for v in data[0][:10]:
    print v


#raw_input("\nany key to continue... ")

d.close()
