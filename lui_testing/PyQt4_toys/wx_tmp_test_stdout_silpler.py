import wx
import sys
import time
from multiprocessing import Pipe, Process
from threading import Thread

class RedirectText2Pipe(object):
    def __init__(self, pipe_inlet):
        self.pipe_inlet = pipe_inlet
    def write(self, string):
        self.pipe_inlet.send(string)
    def flush(self):
        return None

class Run1(Process):
    def __init__(self, pipe_inlet):
        Process.__init__(self)
        self.pipe_std = pipe_inlet

    def run(self):
        redir = RedirectText2Pipe(self.pipe_std)
        sys.stdout = redir
        sys.stderr = redir

        for i in range(20):
            time.sleep(0.2)
            print i,'Hi'

class RedirectedWorkerThread(Thread):
    """Worker Thread Class."""
    def __init__(self, stdout_target):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.stdout_target_ = stdout_target

    def run(self):
        """
        In this function, actually run the process and pull any output from the
        pipes while the process runs
        """
        pipe_outlet, pipe_inlet = Pipe(duplex = False)
        p = Run1(pipe_inlet)
        p.daemon = True
        p.start()

        while p.is_alive():
            #Collect all display output from process
            while pipe_outlet.poll():
                wx.CallAfter(self.stdout_target_.WriteText, pipe_outlet.recv())

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None)

        self.txt1 = wx.TextCtrl(self, style = wx.TE_MULTILINE|wx.TE_READONLY)
        self.btn = wx.Button(self, label='Run')
        self.btn.Bind(wx.EVT_BUTTON, self.OnStart)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.txt1,1,wx.EXPAND)
        sizer.Add(self.btn,1,wx.EXPAND)
        self.SetSizer(sizer)

    def OnStart(self, event):
        t1 = RedirectedWorkerThread(self.txt1)
        t1.daemon = True
        t1.start()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()
