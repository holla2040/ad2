#!/usr/bin/env python

import sys,time
sys.path.append('..')
import AD2

d = AD2.AD2()

d.vposSetOffset = 0.0007
d.vposGetOffset = -0.0007
d.vpos = 1.23

d.vnegSetOffset = 0.0049
d.vnegGetOffset = 0.1195
d.vneg = -1.23

time.sleep(0.5)

print "%8.4f %8.4f %8.4f"%(d.vpos,d.vposSetOffset,d.vposGetOffset)
print "%8.4f %8.4f %8.4f"%(d.vneg,d.vnegSetOffset,d.vnegGetOffset)

raw_input("\nany key to continue... ")

d.close()
