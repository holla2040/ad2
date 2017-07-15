#!/usr/bin/env python

import sys
sys.path.append('..')
import AD2

d = AD2.AD2()

print d.trigger.autotimeoutinfo

d.close()
