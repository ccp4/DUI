def prin_lst(lst, curr):
    for uni in lst:
        stp_str = str(uni.lin_num) + " comm: " + str(uni.my_comm) + " nxt: " + str(uni.nxt_com)
        if( uni.nxt_com is not None ):
            stp_str += " nxt lin: " + str(uni.nxt_com.lin_num)

        if( curr == uni.lin_num ):
            stp_str += " <<< here I am <<<"

        print stp_str

class uni_step(object):
    lin_num = 0
    nxt_com = None
    def __init__(self, parent):
        self.parent = parent
        self.my_comm = None

    def __call__(self, command):
        print "<< running >>", command
        self.my_comm = command
        self.nxt_com = uni_step(self)

class controler(object):
    commands = ['ls', 'echo', 'cat']

    def __init__(self):
        self.step_lst = [uni_step(None)]
        self.bigger_lin = 0
        self.current = self.bigger_lin

    def run(self, command):
        #running "command"
        self.step_lst[self.current](command)

        #creating new empty node
        new_step = self.step_lst[self.current].nxt_com
        self.bigger_lin += 1
        new_step.lin_num = self.bigger_lin
        self.step_lst.append(new_step)

        #doing automatic "goto" to new empty node
        self.current = new_step.lin_num

        #printing new list of steps
        prin_lst(self.step_lst, self.current)

if( __name__ == "__main__"):
    uni_contr = controler()
    for times in xrange(4):
        command = str(raw_input(">>> "))
        uni_contr.run(command)
