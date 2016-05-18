import subprocess
import sys


def test_event_output(line_prn):
    print ">>:", line_prn

print "before subprocess"
p = subprocess.Popen("./sec_interval.sh", stdout = subprocess.PIPE, bufsize = 1, shell = True)
print "after subprocess"
for line in iter(p.stdout.readline, b''):
    single_line = line[0:len(line)-1]
    test_event_output(single_line)

p.stdout.close()
p.wait()

print "after stdout.close()"
