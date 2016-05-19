import subprocess
import sys

def test_event_output(line_prn):
    print "std>> ", line_prn

def test_err_output(err_line_prn):
    print "ERROR>> ", err_line_prn

if(__name__ == "__main__"):

    '''
    p = subprocess.Popen('./sec_interval.sh', stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, bufsize = 1, shell = True)
    '''


    print "starting while loop"

    sub_process = subprocess.Popen('./sec_interval.sh', close_fds=True, shell=True,
                                   bufsize=1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while sub_process.poll() is None:
        out_lin = sub_process.stdout.readline()
        test_event_output(out_lin)

        err_lin = sub_process.stderr.readline()
        test_err_output(err_lin)

        '''
        sys.stdout.write(out)
        sys.stdout.flush()
        '''

    '''
    p.stdout.close()
    p.stderr.close()
    p.wait()
    '''

    print "after ...close()"
