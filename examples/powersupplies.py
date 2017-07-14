#!/usr/bin/env python

import sys,time
sys.path.append('..')
import AD2

d = AD2.AD2()
for i in range(0,51):
    d.vpos = i/10.0
    d.vneg = -i/10.0
    print "%5.2f %5.2f %5.2f"%(i/10.0,d.vpos,d.vneg)
    time.sleep(0.25)
d.close()
