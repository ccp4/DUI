import subprocess

class DialsCommand(object):
    def __init__(self):
        print "creating new DialsCommand (obj)"

    def __call__(self, lst_cmd_to_run = None, ref_to_class = None):
        try:
            print "\n << running >>", lst_cmd_to_run
            my_process = subprocess.Popen(lst_cmd_to_run,
                                          stdout = subprocess.PIPE,
                                          stderr = subprocess.STDOUT,
                                          bufsize = 1)

            for line in iter(my_process.stdout.readline, b''):
                single_line = line[0:len(line)-1]
                try:
                    ref_to_class.emit_print_signal(single_line)

                except:
                    print "<< test >>"
                    print single_line

            my_process.wait()
            my_process.stdout.close()
            if( my_process.poll() == 0 ):
                local_success = True

            else:
                local_success = False

        except:
            local_success = False
            print "\n FAIL call"

        return local_success


def print_list(lst, curr):
    print "__________________________listing:"
    for uni in lst:
        stp_str = str(uni.lin_num) + " comm: " + str(uni.command)

        try:
            stp_str += " prev: " + str(uni.prev_step.lin_num)

        except:
            stp_str += " prev: None"

        stp_str += " nxt: "
        try:
            for nxt_uni in uni.next_step_list:

                stp_str += "  " + str(nxt_uni.lin_num)

        except:
            stp_str += "empty"

        if( curr == uni.lin_num ):
            stp_str += "                           <<< here I am <<<"

        print stp_str

class TreeShow(object):
    def __init__(self):
        self.ind_spc = "      "
        self.ind_lin = "------"

    def __call__(self, my_runner):
        print
        print "status "
        print " |  lin num "
        print " |   |  command "
        print " |   |   | "
        print "------------------"
        self.max_indent = 0
        self.str_lst = []
        self.add_tree(step = my_runner.step_list[0], indent = 0)
        self.tree_print(my_runner.current)
        print "---------------------" + self.max_indent * self.ind_lin


    def add_tree(self, step = None, indent = None):
        if( step.success == True ):
            stp_prn = " S "

        elif( step.success == False ):
            stp_prn = " F "

        else:
            stp_prn = " N "

        str_lin_num = "{0:3}".format(int(step.lin_num))

        stp_prn += str_lin_num + self.ind_spc * indent + "   \___"
        try:
            stp_prn += str(step.command[0])

        except:
            stp_prn += "None"

        self.str_lst.append([stp_prn, indent, int(step.lin_num)])
        try:
            for line in step.next_step_list:
                new_indent = indent + 1
                self.add_tree(step = line, indent = new_indent)

        except:
            new_indent = int(new_indent)
            if( new_indent > self.max_indent ):
                self.max_indent = new_indent


    def tree_print(self, curr):
        self.tree_dat = []
        for tmp_lst in self.str_lst:
            self.tree_dat.append(tmp_lst)

        for pos, loc_lst in enumerate(self.tree_dat):
            if(pos > 0):
                if( loc_lst[1] < self.tree_dat[pos - 1][1] ):
                    for up_pos in xrange(pos - 1, 0, -1):
                        pos_in_str = loc_lst[1] * len(self.ind_spc) + 9
                        left_side = self.tree_dat[up_pos][0][0:pos_in_str]
                        right_side = self.tree_dat[up_pos][0][pos_in_str + 1:]
                        if( self.tree_dat[up_pos][1] > loc_lst[1] ):
                            self.tree_dat[up_pos][0] = left_side + "|" + right_side

                        elif( self.tree_dat[up_pos][1] == loc_lst[1] ):
                            break

            if( loc_lst[2] == curr ):
                lng = len(self.ind_spc) * self.max_indent + 22
                lng_lft = lng - len(self.tree_dat[pos][0])
                str_here = lng_lft * " "
                self.tree_dat[pos][0] += str_here + "   <<< here "

        for prn_str in self.tree_dat:
            print prn_str[0]

