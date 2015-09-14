#!/usr/bin/env ccp4-python

import os, sys
if not "CCP4" in os.environ:
   sys.exit(1)

ccp4 = os.environ["CCP4"]
import pyrvapi
#for item in dir(pyrvapi):
#   print item

#print pyrvapi.RVAPI_MODE_Silent, 'pyrvapi.RVAPI_MODE_Silent'
#print pyrvapi.RVAPI_MODE_Html, 'pyrvapi.RVAPI_MODE_Html'
#print pyrvapi.RVAPI_LAYOUT_Header, 'pyrvapi.RVAPI_LAYOUT_Header'
#print pyrvapi.RVAPI_LAYOUT_Toolbar, 'pyrvapi.RVAPI_LAYOUT_Toolbar'
#print pyrvapi.RVAPI_LAYOUT_Tabs, 'pyrvapi.RVAPI_LAYOUT_Tabs'
#print pyrvapi.RVAPI_LAYOUT_Full, 'pyrvapi.RVAPI_LAYOUT_Full'

from pyrvapi import *
from math import cos, sin
from time import sleep
import subprocess

def makeLogFile(log, nrecords):
   lst = [log]
   for i in range(1,1+nrecords):
      lst.append(" [%4i] Record number %i .....\n" %(i, i))

   return "".join(lst)


def writeLogFile ( f,log,lastPos,p ):
   length = len(log)
   currentPos = lastPos
   lastPos = currentPos + int(length* p)
   if lastPos > length:
      lastPos = length

   if lastPos > currentPos:
      f.write(log[currentPos:lastPos])
      f.flush()

   return lastPos


jsrview = os.path.join(ccp4, "libexec", "jsrview.exe" if sys.platform.startswith('win') else "jsrview")
share_jsrview = os.path.join(ccp4, "share", "jsrview")
dir_data = os.path.join(ccp4, "examples", "toxd")
pdb_inp = os.path.join(dir_data, "toxd.pdb")
mtz_inp = os.path.join(dir_data, "toxd_mapcoefs.mtz")
dir_test = os.path.join(os.getcwd(), "testdir_jsrview")

print "Qt browser:         " + jsrview
print "JavaScript library: " + share_jsrview
print "Mock pdb-output:    " + pdb_inp
print "Mock mtz-output:    " + mtz_inp
print "Working directory:  " + dir_test

if not os.path.isfile(jsrview) or not os.access(jsrview, os.X_OK):
   print "file does not exist or is not executable: %s" %jsrview
   sys.exit(1)

if not os.path.isdir(share_jsrview) or not os.access(share_jsrview, os.X_OK):
   print "directory does not exist or is not accessible: %s" %share_jsrview
   sys.exit(1)

if os.path.exists(dir_test):
   if not os.path.isdir(dir_test):
      print "is not a directory: %s" %dir_test
      sys.exit(1)

   elif not os.access(dir_test, os.X_OK):
      print "directory is not accessible: %s" %dir_test
      sys.exit(1)

else:
   os.mkdir(dir_test)


delay1 = 1.0
delay2 = 1.0
delay3 = 1.0
lastLogPos = 0
print rvapi_init_document ( "TestRun",dir_test,"RVAPI Demo 1",1,7,share_jsrview,None,None,None,None ),
subprocess.Popen([jsrview, os.path.join(dir_test, "index.html")])

