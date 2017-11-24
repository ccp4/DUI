

from CCP4PluginScript import CPluginScript
from CCP4ErrorHandling import *

class gui4xds(CPluginScript):

    TASKTITLE='Dials GUI'  # A short title for gui menu
    TASKNAME = 'dui_lui'   # kind of i2 label
    TASKCOMMAND = 'kate'                    #the program you want to run
    TASKMODULE = 'data_processing'             # Where this plugin will appear on the gui
    TASKVERSION= 0.0                           # Version of this plugin
    ASYNCHRONOUS = True
    TIMEOUT_PERIOD = 9999999.9

    def makeCommandAndScript(self):
      #import CCP4Utils
      #self.appendCommandLine(inp.SEQIN.fullPath ) ] )
      #self.path_wrk = str( self.getWorkDirectory() )
      #par = self.container.controlParameters
      #if par.USE_2d:
      #  self.appendCommandLine(['-2d',self.container.inputData.Directory])
      return CPluginScript.SUCCEEDED

    def processOutputFiles(self):
        self.container.outputData.UNMERGEDFILE.setFullPath(os.path.join(self.workDirectory(),'hklout.mtz'))