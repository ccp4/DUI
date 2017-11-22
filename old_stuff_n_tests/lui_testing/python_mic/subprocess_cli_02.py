'''
import subprocess

if( __name__ == "__main__" ):
    my_process = subprocess.Popen(["../PyQt4_toys/sec_interval.sh"])
    my_process.wait()
'''

import subprocess, time, os, sys
cmd_std_n_err = ["./sec_interval_n_err.sh"]
p = subprocess.Popen(cmd_std_n_err,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)

while True:
    out_str = p.stdout.readline()
    print " :) >>> ", out_str
    err_str = p.stderr.readline()
    print " <<< :( ", err_str
    out_msg = p.poll()
    if( out_msg != None ):
        break

print "out_msg =", out_msg



