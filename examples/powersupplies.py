#!/usr/bin/env python

import sys,time
sys.path.append('..')
import AD2

d = AD2.AD2()

# these are the offsets for my ad2
d.vpos.setOffset = 0.0007
d.vpos.getOffset = -0.0007
d.vneg.setOffset = 0.0049
d.vneg.getOffset = 0.1195

d.vpos.voltage = 1.23
d.vneg.voltage = -1.23

print "%8.4f %8.4f %8.4f"%(d.vpos.voltage,d.vpos.setOffset,d.vpos.getOffset)
print "%8.4f %8.4f %8.4f"%(d.vneg.voltage,d.vneg.setOffset,d.vneg.getOffset)

raw_input("\nany key to continue... ")

d.close()
