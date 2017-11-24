import subprocess

if( __name__ == "__main__" ):
    my_process = subprocess.Popen(["./sec_interval_n_err.sh"])
    my_process.wait()
'''
import subprocess, time, os, sys
cmd_std_n_err = ["./sec_interval_n_err.sh"]

p = subprocess.Popen(cmd_std_n_err,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)

for line in iter(p.stdout.readline, b''):
    print(" :) >>> " + line.rstrip())

for line in iter(p.stderr.readline, b''):
    print(" <<< :( " + line.rstrip())

'''
