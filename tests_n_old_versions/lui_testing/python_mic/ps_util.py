import psutil

def kill_w_child(pid_num):
    print "attempting to kill pid #:", pid_num
    #print "dir(psutil) =", dir(psutil)

    parent = psutil.Process(pid_num)
    for child in parent.children(recursive=True):  # or parent.children() for recursive=False
        child.kill()
    parent.kill()


if(__name__ == "__main__"):
    pid_to_kill = int(raw_input("enter num of pid to kill: "))
    kill_w_child(pid_to_kill)

