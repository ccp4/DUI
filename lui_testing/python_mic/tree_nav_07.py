import sys

def prin_lst(lst, curr):
    print "__________________________listing:"
    for uni in lst:
        stp_str = str(uni.lin_num) + " comm: " + str(uni.my_comm)

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

def show_tree(step = None, curr = None, indent = 1):
    stp_prn = str(step.lin_num) + "  " * indent
    try:
        stp_prn += str(step.my_comm)

    except:
        stp_prn += "None"

    if( step.lin_num == curr ):
        stp_prn += "   <<<<<  "

    print stp_prn
    try:
        for line in step.next_step_list:
            show_tree(step = line, curr = curr, indent = indent + 1)

    except:
        print


class uni_step(object):
    def __init__(self, prev_step):
        self.lin_num = 0
        self.next_step_list = None
        self.prev_step = prev_step
        self.my_comm = None

    def __call__(self, cmd_lst):
        print "____________________________________\n << running >>", cmd_lst
        self.my_comm = cmd_lst

class runner(object):
    commands = ['ls', 'echo', 'cat']

    def __init__(self):
        self.step_list = [uni_step(None)]
        self.bigger_lin = 0
        self.current = self.bigger_lin

    def run(self, command):

        cmd_lst = command.split()
        if( cmd_lst[0] == "goto" ):
            self.goto(int(cmd_lst[1]))

        else:

            if( self.step_list[self.current].my_comm != None ):
                self.goto_prev()
                self.create_step(self.step_list[self.current])

            self.step_list[self.current](cmd_lst)
            self.create_step(self.step_list[self.current])

    def create_step(self, prev_step):
        new_step = uni_step(prev_step)
        self.bigger_lin += 1
        new_step.lin_num = self.bigger_lin
        try:
            if( self.step_list[self.current].next_step_list == None ):
                self.step_list[self.current].next_step_list = [new_step]

            else:
                self.step_list[self.current].next_step_list.append(new_step)

        except:
            print "failed to append to previous step"


        self.step_list.append(new_step)
        self.goto(self.bigger_lin)

    def goto_prev(self):
        print "forking"
        try:
            self.goto(self.step_list[self.current].prev_step.lin_num)

        except:
            print "can NOT fork <None> node "

    def goto(self, new_lin):
        self.current = new_lin

if( __name__ == "__main__"):
    uni_controler = runner()

    command = ""
    while command.strip() != 'exit':
        # printing new list of steps
        prin_lst(uni_controler.step_list, uni_controler.current)

        # showing showing tree
        print "________ showing steps tree:"
        show_tree(step = uni_controler.step_list[0], curr = uni_controler.current, indent = 1)

        try:
            command = str(raw_input(">>> "))

        except:
            print "tweak key pressed ... quitting"
            sys.exit(0)

        uni_controler.run(command)

