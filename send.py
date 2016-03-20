#!/usr/bin/env python
import os,sys

import app
with open(sys.argv[1]) as fp:
  print "Sending %s" % sys.argv[1]
  lineno=1
  for line in fp:
    print "Sendling line #%d" % lineno
    app.serialport.write(line)
    lineno += 1
