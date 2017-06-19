import sys

def prin_lst(lst, curr):
    print "__________________________listing:"
    for uni in lst:
        stp_str = str(uni.lin_num) + " comm: " + str(uni.my_comm)

        try:
            stp_str += " prev: " + str(uni.parent.lin_num)

        except:
            stp_str += " prev: None"

        try:
            stp_str += " nxt: " + str(uni.nxt_com.lin_num)

        except:
            stp_str += " nxt: empty"

        if( curr == uni.lin_num ):
            stp_str += "                           <<< here I am <<<"

        print stp_str

class uni_step(object):
    def __init__(self, parent):
        self.lin_num = 0
        self.nxt_com = None
        self.parent = parent
        self.my_comm = None

    def __call__(self, cmd_lst):
        print "____________________________________\n << running >>", cmd_lst
        self.my_comm = cmd_lst

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

            if( self.step_lst[self.current].my_comm != None ):
                self.create_step(self.step_lst[self.current].parent)

            self.step_lst[self.current](cmd_lst)
            self.create_step(self.step_lst[self.current])

    def create_step(self, parent):
        new_step = uni_step(parent)
        self.bigger_lin += 1
        new_step.lin_num = self.bigger_lin
        self.step_lst.append(new_step)
        self.step_lst[self.current].nxt_com = new_step
        self.goto(self.bigger_lin)


    def goto(self, new_lin):
        self.current = new_lin

if( __name__ == "__main__"):
    uni_controler = runner()

    command = ""
    while command.strip() != 'exit':
        #printing new list of steps
        prin_lst(uni_controler.step_lst, uni_controler.current)
        try:
            command = str(raw_input(">>> "))

        except:
            print "no good input ... quitting"
            sys.exit(0)

        uni_controler.run(command)

