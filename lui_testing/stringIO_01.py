import StringIO
import sys
import time

def func_x(n):
    for iterando in xrange(n):
        print " printing time ", iterando
        time.sleep(1)

old_stdout = sys.stdout

mystdout = StringIO.StringIO()
sys.stdout = mystdout

func_x(3)

sys.stdout = old_stdout

print "\n end StringIO stuff"

lst_stdout = mystdout.getvalue()
print " >>>> \n", lst_stdout , "\n<<<<<"
print "type(lst_stdout) =", type(lst_stdout)

print "counting \\n in lst_stdout"
for pos in lst_stdout:
    if pos == "\n":
        print "found \\n"
