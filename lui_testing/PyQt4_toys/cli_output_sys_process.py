import subprocess
import sys

p = subprocess.Popen("dials.import", stdout = subprocess.PIPE, bufsize = 1, shell = True)
for line in iter(p.stdout.readline, b''):
    print line,
p.stdout.close()
p.wait()

