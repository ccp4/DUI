import subprocess
import sys


def test_event_output(line_prn):
    print "std>> ", line_prn

def test_err_output(err_line_prn):
    print "err>> ", err_line_prn

print "before subprocess"
p = subprocess.Popen("./sec_interval.sh", stdout = subprocess.PIPE,
                     stderr = subprocess.PIPE, bufsize = 1, shell = True)


'''
cmd = "ps -A|grep 'process_name'"
ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = ps.communicate()[0]
print output
'''

print "after subprocess"

for line in iter(p.stdout.readline, b''):
    single_line = line[0:len(line)-1]
    test_event_output(single_line)

for errline in iter(p.stderr.readline, b''):
    single_errline = errline[0:len(errline)-1]
    test_err_output(single_errline)

p.stdout.close()
p.wait()


print "after stdout.close()"
