#!/usr/bin/env python
import os,sys

import app
with open(sys.argv[1]) as fp:
  raw_input("Get lotta ready, then press enter")
  print "Sending %s" % sys.argv[1]
  lineno=1

  if not app.serialport.getCD():
    raise RuntimeError("Lotta is not ready to receive")

  for line in fp:
    print "Sendling line #%d" % lineno
    app.serialport.write(line)
    if not app.serialport.getCD():
      raise RuntimeError("Lotta is not ready to receive anymore")
    lineno += 1
