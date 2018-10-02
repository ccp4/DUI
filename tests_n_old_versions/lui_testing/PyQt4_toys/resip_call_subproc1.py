#import sys, os, subprocess, psutil, time
import sys, os, subprocess, time

def run_my_proc(pickle_path = "", json_path = "",
                command_in = "dials.image_viewer"):

    first_pikl_path = pickle_path[0]
    obj_use_shell = True
    if(obj_use_shell == True):
        cmd_to_run = command_in + " " + str(json_path)
        if(first_pikl_path != None):
            cmd_to_run += " " + str(first_pikl_path)

    else:
        cmd_to_run = [command_in, first_pikl_path, json_path]

    cwd_path = "/tmp/dui_tst/dui_files"

    obj_phil_path = cwd_path + os.sep + "find_spots.phil"
    try:
        os.remove(obj_phil_path)

    except:
        print "no ", obj_phil_path, " found"

    print "\n running Popen>>>", cmd_to_run, ", ", obj_use_shell, "<<< \n"
    obj_my_process = subprocess.Popen(args = cmd_to_run, shell = obj_use_shell,
                                       cwd = cwd_path)

    time.sleep(0.2)
    obj_proc_pid = obj_my_process.pid
    print "obj_proc_pid =", obj_proc_pid
    time.sleep(0.2)

if(__name__ == "__main__"):
    print "Hi 01"
    run_my_proc(pickle_path = ["/tmp/dui_tst/dui_files/10_experiments.json"],
                json_path = "/tmp/dui_tst/dui_files/10_reflections.pickle")
