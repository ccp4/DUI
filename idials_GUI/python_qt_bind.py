'''
DUI's Qt python binding flag

Author: Luis Fuentes-Montero (Luiso)
With strong help from DIALS and CCP4 teams

copyright (c) CCP4 - DLS
'''

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


'''
#This is the only variable that needs to be changed if you want
#the hole GUI to depend on a different Qt binding
'''

pyhon_binding = "PyQt4"
#pyhon_binding = "PySide"

if pyhon_binding == "PyQt4":
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    from PyQt4.QtWebKit import *
    from PyQt4.QtOpenGL import QGLWidget
    print "   <<<   using PyQt4"

else:
    #asuming GuiBinding.pyhon_binding == "PySide"
    from PySide.QtGui import *
    from PySide.QtCore import *
    from PySide.QtWebKit import *
    from PySide.QtOpenGL import QGLWidget
    pyqtSignal = Signal
    print "using PySide"


