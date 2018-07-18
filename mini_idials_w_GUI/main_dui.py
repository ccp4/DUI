'''
DUI's main Widget launcher

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

import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

from m_idials_gui import MainWidget
from cli_utils import sys_arg

def main():
    call_arg = sys.argv
    if(len(call_arg) > 1):
        for par_str in call_arg[1:]:
            if(par_str == "e" or par_str == "-e" or
                    par_str == "explicit" or par_str == "--explicit"):

                sys_arg.make_next = False
                sys_arg.run_all = False
                print "Running in << explicit >> mode"

            elif(par_str == "a" or par_str == "-a" or
                 par_str == "automatic" or par_str == "--automatic"):

                sys_arg.make_next = True
                sys_arg.run_all = False
                print "Running in << automatic >> mode"

            elif(par_str == "sa" or par_str == "-sa" or
                 par_str == "superautomatic" or par_str == "--superautomatic"):

                sys_arg.make_next = True
                sys_arg.run_all = True
                print "Running in << SUPER automatic >> mode"

            elif(par_str[0:9] == "template="):
                sys_arg.template = par_str[9:]

            elif(par_str[0:10] == "directory="):
                sys_arg.directory = par_str[10:]

    print "sys_arg.template=", sys_arg.template
    print "sys_arg.directory=", sys_arg.directory
    app =  QApplication(call_arg)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())

if(__name__ == "__main__"):
    main()
