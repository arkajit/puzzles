#!/usr/bin/python
# puzzle: hoppity
# lang: Python
# author: arkajit (arkajit.dey@gmail.com)

import sys

if len(sys.argv) == 2:
  n = 0

  try:
    f = open(sys.argv[1], 'r')
    s = f.read().split()[0]
    n = int(s)
  except IOError:
    print "Error: Could not open file"
  
  for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
      print "Hop"
    elif i % 3 == 0:
      print "Hoppity"
    elif i % 5 == 0:
      print "Hophop"
