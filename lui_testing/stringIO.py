from cStringIO import StringIO
import sys

old_stdout = sys.stdout

mystdout = StringIO()
sys.stdout = mystdout

for iterando in xrange(5):
    print " printing time ", iterando

sys.stdout = old_stdout

print "\n end StringIO stuff"

lst_stdout = mystdout.getvalue()
print " >>>> \n", lst_stdout , "\n<<<<<"
