from cStringIO import StringIO
import sys

def func_x(n):
    for iterando in xrange(n):
        print " printing time ", iterando


old_stdout = sys.stdout

mystdout = StringIO()
sys.stdout = mystdout

func_x(5)

sys.stdout = old_stdout

print "\n end StringIO stuff"

lst_stdout = mystdout.getvalue()
print " >>>> \n", lst_stdout , "\n<<<<<"
print "type(lst_stdout) =", type(lst_stdout)

print "counting \\n in lst_stdout"
for pos in lst_stdout:
    if pos == "\n":
        print "found \\n"
