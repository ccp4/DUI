from string import Template
import os
from CCP4Dispatchers import dispatcher_builder

cmd = '''HKLIN hklout.mtz
HKLOUT unscaled.mtz'''

#keywords = """LABIN FP=FNAT SIGFP=SIGFNAT FREE=FreeR_flag
#NCYC 10
#END
#"""

#f1 = open("job.log","w")
#f2 = open("job.err","w")

d = dispatcher_builder("pointless", cmd)
d.call(wait=False)


while d.isRunning:
    stdout_line, stderr_line = d.monitor()

    # Do something with stdout_line. If the job is going badly, can
    # call d.abort()
    if stdout_line: print ">>>>", stdout_line.rstrip()
    if stderr_line: print "err>", stderr_line.rstrip()

print d.stderr_data
# if d.call_val is 0 then there was no error but 1 means error
print d.call_val
#f1.close()
#f2.close()
