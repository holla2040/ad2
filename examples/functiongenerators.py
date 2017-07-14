#!/usr/bin/env python

import sys,time
sys.path.append('..')
import AD2

d = AD2.AD2()

# these are the offsets for my ad2
d.fg1.frequency = 1000
d.fg1.amplitude = 1.23
d.fg1.offset    = -1.23

d.fg2.frequency = 2000
d.fg2.amplitude = 2.23
d.fg2.offset    = -2.23

print "%10.2f %10.2f %10.2f"%(d.fg1.frequency,d.fg1.amplitude,d.fg1.offset)
print "%10.2f %10.2f %10.2f"%(d.fg2.frequency,d.fg2.amplitude,d.fg2.offset)

raw_input("\nany key to continue... ")

d.close()
