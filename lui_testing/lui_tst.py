#!/usr/bin/env ccp4-python

import os, sys
if not "CCP4" in os.environ:
   sys.exit(1)

ccp4 = os.environ["CCP4"]
import pyrvapi

from pyrvapi import *
import subprocess


#from math import cos, sin
from time import sleep


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


delay1 = 2.0

lastLogPos = 0
print rvapi_init_document ( "TestRun",dir_test,"RVAPI Demo 1",1,7,share_jsrview,None,None,None,None ),
subprocess.Popen([jsrview, os.path.join(dir_test, "index.html")])

# Starting to test new code here
#______________________________________________________________________________________________________

rvapi_add_header ( "DUI Demo Page 1" )

print rvapi_add_tab    ( "single_tab","DIALS U. I.",True ),

#if (delay1>0):  sleep ( delay1 )
print rvapi_add_section  ( "sec1","Control"   ,"single_tab",0,0,1,1,True ),
print rvapi_add_section1 ( "single_tab/sec2","Logs or CLI outputs",1,0,1,1,True ),
print rvapi_flush(),


print rvapi_add_text ( "To run in CLI","sec1",0,0,1,1 ),
print rvapi_add_text ( "some log here \n<br>" "or\n<br>" " command line output","sec2",0,0,1,1 ),

print rvapi_add_line_edit ( "CLI_input", "command line input", "Empty for now", 40, "sec1",1,0,2,40)
print rvapi_add_button ( "GO_button", "Go", "ls", "prv_01", False , "sec1",2,0,5,40);

print rvapi_flush()

##################################################################################

print rvapi_add_tree_widget ( "panel_container","","sec1",0,0,1,1 ),
print rvapi_add_panel      ( "tree_panel_1","panel_container",0,0,1,1 ),
print rvapi_add_text      ( "Text inside panel 1","tree_panel_1",0,0,1,1 ),
print rvapi_set_tree_node ( "panel_container","tree_panel_1","Graph 1","auto","" ),
print rvapi_add_panel     ( "tree_panel_2","panel_container",0,0,1,1 ),
print rvapi_add_text      ( "Another text in another panel","tree_panel_2",0,0,1,1 ),
print rvapi_set_tree_node ( "panel_container","tree_panel_2","Text 2","auto","" ),
