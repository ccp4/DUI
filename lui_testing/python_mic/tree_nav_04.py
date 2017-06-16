import sys

def prin_lst(lst, curr):
    for uni in lst:
        stp_str = str(uni.lin_num) + " comm: " + str(uni.my_comm) + " nxt: " + str(uni.nxt_com)
        if( uni.nxt_com is not [None] ):
            stp_str += " nxt lin: " + str(uni.nxt_com[1].lin_num)

        if( curr == uni.lin_num ):
            stp_str += " <<< here I am <<<"

        print stp_str

class uni_step(object):
    lin_num = 0
    nxt_com = [None]
    def __init__(self, parent):
        self.parent = parent
        self.my_comm = None

    def __call__(self, cmd_lst):
        print "<< running >>", cmd_lst
        self.my_comm = cmd_lst
        self.nxt_com.append(uni_step(self))

class runner(object):
    commands = ['ls', 'echo', 'cat']

    def __init__(self):
        self.step_lst = [uni_step(None)]
        self.bigger_lin = 0
        self.current = self.bigger_lin

    def run(self, command):
        #running "command"
        cmd_lst = command.split()
        if( cmd_lst[0] == "goto" ):
            self.goto(int(cmd_lst[1]))

        else:
            self.step_lst[self.current](cmd_lst)

            #creating new empty node
            new_step = self.step_lst[self.current].nxt_com[1]
            self.bigger_lin += 1
            new_step.lin_num = self.bigger_lin
            self.step_lst.append(new_step)

            #doing automatic "goto" to new empty node
            self.goto(new_step.lin_num)

    def goto(self, new_lin):
        self.current = new_lin

if( __name__ == "__main__"):
    uni_contr = runner()
    for times in xrange(9999):
        try:
            command = str(raw_input(">>> "))

        except:
            print "no good input? , quitting"
            sys.exit(0)

        uni_contr.run(command)


        #printing new list of steps
        prin_lst(uni_contr.step_lst, uni_contr.current)
