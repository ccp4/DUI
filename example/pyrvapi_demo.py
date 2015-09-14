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

# ****************************************************************
#   DEMO 1:  MAKING TABS
# ****************************************************************

if (delay1>0):  sleep ( delay1 )
print rvapi_add_header ( "RVAPI Demo Page 1" ),
#  print rvapi_add_tab    ( "tab1","Report"  ,True  ),
print rvapi_add_tab    ( "tab2","Log file",False ),
print rvapi_insert_tab ( "tab1","Report","tab2",True  ),

# Add watched (updatable) content to the log tab. Note that the
# log file does not exist yet.
log = dir_test + "/output.log"
print rvapi_append_content ( log,True,"tab2" ),

# Flush will push incremental changes into browser
print rvapi_flush(),


# ****************************************************************
#   DEMO 2:  MAKING SECTIONS IN TABS
# ****************************************************************

if (delay1>0):  sleep ( delay1 )
print rvapi_add_section  ( "sec1","Results"   ,"tab1",0,0,1,1,True ),
print rvapi_add_section1 ( "tab1/sec2","Output files",1,0,1,1,True ),
print rvapi_flush(),

# Start log output just now, after two flushes, so that the log
# appears in the log tab with a noticeable delay
f = open ( log,"w" )
log = makeLogFile ( log,1000 )

# ****************************************************************
#   DEMO 3:  PUTTING TEXTS INTO SECTIONS
# ****************************************************************

if (delay1>0):  sleep ( delay1 )
lastLogPos = writeLogFile ( f,log,lastLogPos,0.035 )

# Note that one can put text straight into tab grids just as well,
# by specifying tab ids instead of section ids in the following
# functions
print rvapi_add_text ( "Something about results.","sec1",0,0,1,1 ),
print rvapi_add_text ( "This test is only for demonstration.\n<br>"
                 "This text contains a newline symbol","sec2",
                 0,0,1,1 ),
print rvapi_flush(),


# ****************************************************************
#   DEMO 3:  MAKING TABLES
# ****************************************************************

if (delay1>0):  sleep ( delay1 )
lastLogPos = writeLogFile ( f,log,lastLogPos,0.071 )

# We put this table into a section, however it can be put anywhere
# by just specifying an appropriate node Id
print rvapi_add_table1 ( "sec1/table1","Demo Table 1",1,0,1,1, 1 ),
#  print rvapi_add_table1 ( "sec1/table1","",1,0,1,1, 0 ),

# Make column headers (optional)
print rvapi_put_horz_theader ( "table1","Column 1","Tooltip 1",0 ),
print rvapi_put_horz_theader ( "table1","Column 2","",1 ),
print rvapi_put_horz_theader ( "table1","Column 3","Tooltip 2",2 ),
print rvapi_put_horz_theader ( "table1","Column 4","",3 ),

# Make row headers (optional)
print rvapi_put_vert_theader ( "table1","Row 1","Tooltip 1",0 ),
print rvapi_put_vert_theader ( "table1","** Row 2 **","",1 ),

# Fill table body. Any strings may be put in, however, there are
# interface functions for other types of data. Note that one
# can leave empty cells and intersperse data types at will
for i in range(0,2):
  for j in range(0,4):

    S = "%10.3g" %( float(i+1)*float(j+1)/3.14159265 )
    print rvapi_put_table_string ( "table1",S,i,j ),

print rvapi_flush(),

print rvapi_add_table1 ( "sec1/table2","Header",2,0,1,1, 100 ),

# Make column headers (optional)
print rvapi_put_horz_theader ( "table2","Column 1","Tooltip 1",0 ),
print rvapi_put_horz_theader ( "table2","Column 2","",1 ),
print rvapi_put_horz_theader ( "table2","Column 3","Tooltip 2",2 ),
print rvapi_put_horz_theader ( "table2","Column 4","",3 ),

# Make row headers (optional)
print rvapi_put_vert_theader ( "table2","Row 1","Tooltip 1",0 ),
print rvapi_put_vert_theader ( "table2","** Row 2 **","",1 ),

# Fill table body. Any strings may be put in, however, there are
# interface functions for other types of data. Note that one
# can leave empty cells and intersperse data types at will
for i in range(0,2):
  for j in range(0,4):

    S = "%10.3g" %( float(i+1)*float(j+1)/3.14159265 )
    print rvapi_put_table_string ( "table2",S,i,j ),

print rvapi_shape_table_cell   ( "table2",0,3,"","width:100%;","",1,1 ),

print rvapi_flush(),


# ****************************************************************
#   DEMO 4:  MAKING DATA WIDGETS
# ****************************************************************

if (delay1>0):  sleep ( delay1 )
lastLogPos = writeLogFile ( f,log,lastLogPos,0.05 )

print rvapi_add_data1 ( "sec2/dat1","Structure and electron density",
                pdb_inp,
                "xyz",2,0,1,1,1 ),
print rvapi_append_to_data ( "dat1",
                mtz_inp,
                "hkl:map" ),
print rvapi_flush(),


# ****************************************************************
#   DEMO 5:  APPENDING, RATHER THAN SETTING WIDGETS ON THE PAGE
# ****************************************************************

if (delay2>0):  sleep ( delay2 )
lastLogPos = writeLogFile ( f,log,lastLogPos,0.09 )

# In "append" mode, the row grid counter autoincrements, and only
# 0th column is used for placing new element in the page
print rvapi_append_text ( "This demonstrates the 'append' style of API "
                    "functions.<br>&nbsp;","sec1" ),


# ****************************************************************
#   DEMO 5:  MAKING A GRAPH WIDGET
# ****************************************************************

if (delay2>0):  sleep ( delay2 )
lastLogPos = writeLogFile ( f,log,lastLogPos,0.03 )

# We choose to put a graph widget into 1st section, although it may
# be placed anywhere
print rvapi_append_loggraph1 ( "sec1/graphWidget1" ),

# Graph widgets contain lists of data and lists of plots. First, we
# describe a single data block, containing x-points and 4 functions
# on them. Note that any ids for X- and Y- values may be chosen, and
# that they are local to the data block.
print rvapi_add_graph_data1    ( "graphWidget1/data1","Trigonometry" ),
print rvapi_add_graph_dataset1 ( "graphWidget1/data1/x","x","argument" ),
print rvapi_add_graph_dataset1 ( "graphWidget1/data1/y1","sin(x)","Sine" ),
print rvapi_add_graph_dataset1 ( "graphWidget1/data1/y2","cos(x)","Cosine" ),
print rvapi_add_graph_dataset1 ( "graphWidget1/data1/y3","sin(x)/x","Damped sine" ),
print rvapi_add_graph_dataset1 ( "graphWidget1/data1/y4","cos(x)/x","Damped cosine" ),

# Now put XY data
for i in range(1,21):
  print rvapi_add_graph_int1  ( "graphWidget1/data1/x",i ),
  print rvapi_add_graph_real1 ( "graphWidget1/data1/y1",sin(i*6.28/19.0),"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget1/data1/y2",cos(i*6.28/19.0),"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget1/data1/y3",sin(i*6.28/19.0)/i,"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget1/data1/y4",cos(i*6.28/19.0)/i,"%g" ),


# Second, we describe individual plots, which will be switchable in
# the right-hand side of the graph widget.

print rvapi_add_graph_plot1 ( "graphWidget1/plot1","Sine and Cosine",
                        "Argument","Functions: Sine and Cosine" ),
print rvapi_add_plot_line1  ( "graphWidget1/data1/plot1","x","y1" ),
print rvapi_add_plot_line1  ( "graphWidget1/data1/plot1","x","y2" ),
print rvapi_set_plot_xmin   ( "plot1","graphWidget1",-1.0 ),

print rvapi_set_line_fill1  ( "graphWidget1/data1/plot1/y1",
                        True,True,RVAPI_COLOR_LightCoral,0.2 ),
print rvapi_set_line_fill1  ( "graphWidget1/data1/plot1/y2",
                        True,True,RVAPI_COLOR_Aquamarine,0.2 ),


print rvapi_add_graph_plot1 ( "graphWidget1/plot2","Damped sine and cosine",
                      "Argument","Functions: Damped Sine and Cosine" ),
print rvapi_add_plot_line1  ( "graphWidget1/data1/plot2","x","y3" ),
print rvapi_add_plot_line1  ( "graphWidget1/data1/plot2","x","y4" ),
print rvapi_set_plot_xmax   ( "plot2","graphWidget1",50.0 ),

# Finally, push changes into the browser.
print rvapi_flush(),


# ****************************************************************
#   DEMO 6:  ADDING DATA TO GRAPH WIDGET - 1
# ****************************************************************

if (delay2>0):  sleep ( delay2 )
lastLogPos = writeLogFile ( f,log,lastLogPos,0.065 )

# Adding data is quite straightforward. In this example, we just
# create another data block, fill it with data and describe the
# corresponding plots by just repeating the same steps as in Demo 5.

print rvapi_add_graph_data1    ( "graphWidget1/data2","Powers" ),
print rvapi_add_graph_dataset1 ( "graphWidget1/data2/x","x","argument" ),
print rvapi_add_graph_dataset1 ( "graphWidget1/data2/y1","x^2","Direct square" ),
print rvapi_add_graph_dataset1 ( "graphWidget1/data2/y2","x^3","Direct power 3" ),
print rvapi_add_graph_dataset1 ( "graphWidget1/data2/y3","x^{-2}","Inverse square" ),
print rvapi_add_graph_dataset1 ( "graphWidget1/data2/y4","x^{-3}","Inverse power 3" ),

for i in range(1,21):
  x = (i-10.5)/10.0
  print rvapi_add_graph_real1 ( "graphWidget1/data2/x",x,"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget1/data2/y1",x*x,"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget1/data2/y2",x*x*x,"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget1/data2/y3",0.99999995/(x*x),"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget1/data2/y4",0.1/(x*x*x),"%g" ),


# Here we describe new plots #3 and #4, placing them under the title
# of datablock 'data2'. Note, thoughm that they can be placed under
# the title of datablock 'data1' just as well. Note also, that plots
# can use data from different datablocks. Note finally, that
# datablock may be empty and used only for providing a collective
# title for a series of plots.

print rvapi_add_graph_plot1 ( "graphWidget1/plot3","Direct powers",
                      "Argument","Functions: Powers x^2 and x^3" ),
print rvapi_add_plot_line1 ( "graphWidget1/data2/plot3","x","y1" ),
print rvapi_add_plot_line1 ( "graphWidget1/data2/plot3","x","y2" ),

print rvapi_add_graph_plot1 ( "graphWidget1/plot4","Inverse powers",
                      "Argument","Functions: Powers x^{-2} and x^{-3}" ),
print rvapi_add_plot_line1 ( "graphWidget1/data2/plot4","x","y3" ),
print rvapi_add_plot_line1 ( "graphWidget1/data2/plot4","x","y4" ),

print rvapi_flush(),


# ****************************************************************
#   DEMO 7:  ADDING DATA TO GRAPH WIDGET - 2
# ****************************************************************

if (delay2>0):  sleep ( delay2 )
lastLogPos = writeLogFile ( f,log,lastLogPos,0.085 )

# In this example, we add XY points to the existing data block.
# All relevant plots will update automatically in the browser as
# soon as content is flushed.

for i in range(21,41):
  print rvapi_add_graph_int1  ( "graphWidget1/data1/x",i ),
  print rvapi_add_graph_real1 ( "graphWidget1/data1/y1",sin(i*6.28/19.0),"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget1/data1/y2",cos(i*6.28/19.0),"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget1/data1/y3",sin(i*6.28/19.0)/i,"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget1/data1/y4",cos(i*6.28/19.0)/i,"%g" ),


print rvapi_flush(),


# ****************************************************************
#   DEMO 8:  ADDING DATA TO GRAPH WIDGET - 3
# ****************************************************************

if (delay2>0):  sleep ( delay2 )
lastLogPos = writeLogFile ( f,log,lastLogPos,0.025 )

# In this example, we add both data to a data block and a new plot
# to the list of plots.

print rvapi_add_graph_dataset1 ( "graphWidget1/data1/y5","x*sin(x)","Amplified sine" ),
print rvapi_add_graph_dataset1 ( "graphWidget1/data1/y6","x*cos(x)","Amplified cosine" ),

# Note that X-points in the selected data block already run from
# 1 to 40, from previous updates. However, it is Ok to provide new
# Y-values only for a subset of them, e.g, in range of 1-20.
for i in range(1,21):
  print rvapi_add_graph_real1 ( "graphWidget1/data1/y5",i*sin(i*6.28/19.0),"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget1/data1/y6",i*cos(i*6.28/19.0),"%g" ),


print rvapi_add_graph_plot1 ( "graphWidget1/plot5","Amplified sine and cosine",
                      "Argument","Functions: Amplified Sine and Cosine" ),
print rvapi_add_plot_line1 ( "graphWidget1/data1/plot5","x","y5" ),
print rvapi_add_plot_line1 ( "graphWidget1/data1/plot5","x","y6" ),

# set custom x-scale
for i in range(-2,25,2):

  S = "[%i]" %( (22-i)*(22-i) )
  print rvapi_add_plot_xtick1 ( "graphWidget1/plot5",i,S ),


print rvapi_flush(),



# ****************************************************************
#   DEMO 9:  MAKING TREE WIDGETS
# ****************************************************************

if (delay2>0):  sleep ( delay2 )
lastLogPos = writeLogFile ( f,log,lastLogPos,0.095 )

print rvapi_add_tab ( "tree_tab","Tree Widget",True ),

print rvapi_add_tree_widget ( "tree1","Tree Example","tree_tab",0,0,1,1 ),

print rvapi_add_section ( "tree_sec1","Section for NODE 1","tree1",0,0,1,1,True ),
print rvapi_add_text    ( "Text for NODE 1","tree_sec1",0,0,1,1 ),
print rvapi_add_section ( "tree_sec2","Section for NODE 2","tree1",0,0,1,1,True ),
print rvapi_add_text    ( "Text for NODE 2","tree_sec2",0,0,1,1 ),
print rvapi_add_section ( "tree_sec21","Section for NODE 21","tree1",0,0,1,1,True ),
print rvapi_add_text    ( "Text for NODE 21","tree_sec21",0,0,1,1 ),
print rvapi_add_section ( "tree_sec22","Section for NODE 22","tree1",0,0,1,1,True ),
print rvapi_add_text    ( "Text for NODE 22","tree_sec22",0,0,1,1 ),

print rvapi_set_tree_node ( "tree1","tree_sec1","Node 1","auto","" ),
print rvapi_set_tree_node ( "tree1","tree_sec2","Node 2","open","" ),
print rvapi_set_tree_node ( "tree1","tree_sec21","Node 21 make this long","auto","tree_sec2" ),
print rvapi_set_tree_node ( "tree1","tree_sec22","Node 22","auto","tree_sec2" ),

print rvapi_flush(),

if (delay2>0):  sleep ( delay2 )
#  print rvapi_add_text    ( "Another Text for NODE 1","tree_sec1",1,0,1,1 ),
print rvapi_append_text    ( "Another Text for NODE 1","tree_sec1" ),
print rvapi_flush(),


# ****************************************************************
#   DEMO 10:  MAKING RADAR WIDGETS
# ****************************************************************

if (delay2>0):  sleep ( delay2 )
lastLogPos = writeLogFile ( f,log,lastLogPos,0.1 )

print rvapi_add_radar ( "radar1","Radar example","tree_tab",1,0,1,1,0 ),
print rvapi_add_radar_property ( "radar1","prop 1",0.1 ),
print rvapi_add_radar_property ( "radar1","prop 2",0.5 ),
print rvapi_add_radar_property ( "radar1","prop 3",0.3 ),
print rvapi_add_radar_property ( "radar1","prop 4",0.9 ),
print rvapi_add_radar_property ( "radar1","prop 5",1.0 ),
print rvapi_add_radar_property ( "radar1","prop 6",0.7 ),

print rvapi_flush(),



# ****************************************************************
#   DEMO 11:  UPDATING GRAPHS IN TREE LEAFS
# ****************************************************************

if (delay3>0):  sleep ( delay3 )
lastLogPos = writeLogFile ( f,log,lastLogPos,0.105 )

print rvapi_add_tab ( "tree_graph_tab","Tree Widget with Graphs",True ),

print rvapi_add_tree_widget ( "tree2","Tree Graph Example","tree_graph_tab",0,0,1,1 ),

# We choose to put a graph widget into 1st section, although it may
# be placed anywhere
print rvapi_add_loggraph    ( "graphWidget2","tree2",0,0,1,1 ),

# Graph widgets contain lists of data and lists of plots. First, we
# describe a single data block, containing x-points and 4 functions
# on them. Note that any ids for X- and Y- values may be chosen, and
# that they are local to the data block.
print rvapi_add_graph_data1    ( "graphWidget2/data21","Trigonometry" ),
print rvapi_add_graph_dataset1 ( "graphWidget2/data21/x","x","argument" ),
print rvapi_add_graph_dataset1 ( "graphWidget2/data21/y1","sin(x)","Sine" ),
print rvapi_add_graph_dataset1 ( "graphWidget2/data21/y2","cos(x)","Cosine" ),
print rvapi_add_graph_dataset1 ( "graphWidget2/data21/y3","sin(x)/x","Damped sine" ),
print rvapi_add_graph_dataset1 ( "graphWidget2/data21/y4","cos(x)/x","Damped cosine" ),

# Now put XY data
for i in range(1,21):
  print rvapi_add_graph_int1  ( "graphWidget2/data21/x",i ),
  print rvapi_add_graph_real1 ( "graphWidget2/data21/y1",sin(i*6.28/19.0),"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget2/data21/y2",cos(i*6.28/19.0),"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget2/data21/y3",sin(i*6.28/19.0)/i,"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget2/data21/y4",cos(i*6.28/19.0)/i,"%g" ),


# Second, we describe individual plots, which will be switchable in
# the right-hand side of the graph widget.

print rvapi_add_graph_plot1   ( "graphWidget2/plot21","Sine and Cosine",
                          "Argument","Functions: Sine and Cosine" ),
print rvapi_add_plot_line1    ( "graphWidget2/data21/plot21","x","y1" ),
print rvapi_set_line_options1 ( "graphWidget2/data21/plot21/y1",
                          RVAPI_COLOR_IndianRed,
                          RVAPI_LINE_Bars,RVAPI_MARKER_filledCircle,
                          1.0, True ),

print rvapi_add_plot_line1  ( "graphWidget2/data21/plot21","x","y2" ),
print rvapi_set_line_options1 ( "graphWidget2/data21/plot21/y2",
                          RVAPI_COLOR_Gold,
                          RVAPI_LINE_Off,RVAPI_MARKER_filledCircle,
                          2.5, True ),

print rvapi_add_graph_plot1 ( "graphWidget2/plot22","Damped sine and cosine",
                      "Argument","Functions: Damped Sine and Cosine" ),
print rvapi_add_plot_line1  ( "graphWidget2/data21/plot22","x","y3" ),
print rvapi_add_plot_line1  ( "graphWidget2/data21/plot22","x","y4" ),

print rvapi_set_plot_xrange ( "plot22","graphWidget2",0.0,40.0 ),
print rvapi_set_plot_yrange ( "plot22","graphWidget2",-0.4,1.2 ),

print rvapi_set_tree_node ( "tree2","graphWidget2","Graph 1","auto","" ),

# Finally, push changes into the browser.
print rvapi_flush(),


# ****************************************************************
#   DEMO 12:  ADDING DATA TO GRAPH WIDGET IN TREE LEAF
# ****************************************************************

if (delay3>0):  sleep ( delay3 )
lastLogPos = writeLogFile ( f,log,lastLogPos,0.11 )

# Adding data is quite straightforward. In this example, we just
# create another data block, fill it with data and describe the
# corresponding plots by just repeating the same steps as in Demo 5.

print rvapi_add_graph_data1    ( "graphWidget2/data22","Powers" ),
print rvapi_add_graph_dataset1 ( "graphWidget2/data22/x","x","argument" ),
print rvapi_add_graph_dataset1 ( "graphWidget2/data22/y1","x^2","Direct square" ),
print rvapi_add_graph_dataset1 ( "graphWidget2/data22/y2","x^3","Direct power 3" ),
print rvapi_add_graph_dataset1 ( "graphWidget2/data22/y3","x^{-2}","Inverse square" ),
print rvapi_add_graph_dataset1 ( "graphWidget2/data22/y4","x^{-3}","Inverse power 3" ),

for i in range(1,21):
  x = (i-10.5)/10.0
  print rvapi_add_graph_real1 ( "graphWidget2/data22/x",x,"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget2/data22/y1",x*x,"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget2/data22/y2",x*x*x,"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget2/data22/y3",0.99999995/(x*x),"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget2/data22/y4",0.1/(x*x*x),"%g" ),


# Here we describe new plots #23 and #24, placing them under the title
# of datablock 'data2'. Note, thoughm that they can be placed under
# the title of datablock 'data1' just as well. Note also, that plots
# can use data from different datablocks. Note finally, that
# datablock may be empty and used only for providing a collective
# title for a series of plots.

print rvapi_add_graph_plot1 ( "graphWidget2/plot23","Direct powers",
                        "Argument","Functions: Powers x^2 and x^3" ),
print rvapi_add_plot_line1  ( "graphWidget2/data22/plot23","x","y1" ),
print rvapi_add_plot_line1  ( "graphWidget2/data22/plot23","x","y2" ),

print rvapi_add_graph_plot1 ( "graphWidget2/plot24","Inverse powers",
                        "Argument","Functions: Powers x^{-2} and x^{-3}" ),
print rvapi_add_plot_line1  ( "graphWidget2/data22/plot24","x","y3" ),
print rvapi_add_plot_line1  ( "graphWidget2/data22/plot24","x","y4" ),

print rvapi_flush(),



# ****************************************************************
#   DEMO 13:  ADDING DATA TO GRAPH WIDGET IN TREE LEAF - 2
# ****************************************************************

if (delay3>0):  sleep ( delay3 )
lastLogPos = writeLogFile ( f,log,lastLogPos,0.115 )

# In this example, we add XY points to the existing data block.
# All relevant plots will update automatically in the browser as
# soon as content is flushed.

for i in range(21,41):
  print rvapi_add_graph_int1  ( "graphWidget2/data21/x",i ),
  print rvapi_add_graph_real1 ( "graphWidget2/data21/y1",sin(i*6.28/19.0),"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget2/data21/y2",cos(i*6.28/19.0),"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget2/data21/y3",sin(i*6.28/19.0)/i,"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget2/data21/y4",cos(i*6.28/19.0)/i,"%g" ),
  sleep ( delay3 )
  print rvapi_flush(),


print rvapi_flush(),


# ****************************************************************
#   DEMO 14:  ADDING DATA TO GRAPH WIDGET IN TREE LEAF - 3
# ****************************************************************

if (delay3>0):  sleep ( delay3 )
lastLogPos = writeLogFile ( f,log,lastLogPos,0.025 )

# In this example, we add both data to a data block and a new plot
# to the list of plots.

print rvapi_add_graph_dataset1 ( "graphWidget2/data21/y5","x*sin(x)","Amplified sine" ),
print rvapi_add_graph_dataset1 ( "graphWidget2/data21/y6","x*cos(x)","Amplified cosine" ),

# Note that X-points in the selected data block already run from
# 1 to 40, from previous updates. However, it is Ok to provide new
# Y-values only for a subset of them, e.g, in range of 1-20.
for i in range(1,21):
  print rvapi_add_graph_real1 ( "graphWidget2/data21/y5",i*sin(i*6.28/19.0),"%g" ),
  print rvapi_add_graph_real1 ( "graphWidget2/data21/y6",i*cos(i*6.28/19.0),"%g" ),


print rvapi_add_graph_plot1 ( "graphWidget2/plot25","Amplified sine and cosine",
                      "Argument","Functions: Amplified Sine and Cosine" ),
print rvapi_add_plot_line1 ( "graphWidget2/data21/plot25","x","y5" ),
print rvapi_add_plot_line1 ( "graphWidget2/data21/plot25","x","y6" ),

print rvapi_flush(),


if (delay3>0):  sleep ( delay3 )
lastLogPos = writeLogFile ( f,log,lastLogPos,0.12 )

print rvapi_add_panel     ( "tree_panel_2","tree2",0,0,1,1 ),
print rvapi_add_text      ( "JUST A PLLACEHOLDER FOR TREE LEAF","tree_panel_2",0,0,1,1 ),
print rvapi_set_tree_node ( "tree2","tree_panel_2","Text 2","auto","" ),

print rvapi_flush(),

# flush all log
lastLogPos = writeLogFile ( f,log,lastLogPos,1.0 )
f.close()


print



