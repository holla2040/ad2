#!/usr/bin/env python

import sys,time
sys.path.append('..')
import AD2
from AD2.dwfconstants import *


d = AD2.AD2()

'''
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
'''


d.scope.buffersize              = 1024
d.scope.frequency               = 1000000.0
d.scope.trigger.type            = trigtypeEdge
d.scope.trigger.channel         = 0
d.scope.trigger.level           = 0.29
d.scope.trigger.condition       = trigcondRisingPositive
d.scope.trigger.hysteresis      = 0.01

d.scope.trigger.position        = -0.0004885
d.scope.trigger.length          = 0.1
d.scope.trigger.lengthcondition = triglenLess

print d.scope.trigger.positioninfo


time.sleep(2)

d.scope.single()
data = d.scope.read()
# print data

stepsize = 1/d.scope.frequency

#for i in range(450,550):
for i in range(50):
    print "%05d %10.6f %10.6f"%(i,stepsize*i,data[0][i])


#raw_input("\nany key to continue... ")

d.close()
