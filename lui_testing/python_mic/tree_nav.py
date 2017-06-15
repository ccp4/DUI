def prin_lst(lst):
    for u_stp in lst:
        print u_stp.lin_num, "my_comm:", u_stp.my_comm

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
    commands = ['goto', 'goup', 'godown', 'ls', 'echo', 'cat']

    def __init__(self):
        self.step_lst = [uni_step(None)]
        self.bigger_lin = 0
        self.current = self.bigger_lin

    def __call__(self, command):
        self.bigger_lin += 1
        self.step_lst[self.current](command)
        new_step = self.step_lst[self.current].nxt_com
        new_step.lin_num = self.bigger_lin
        self.current = new_step.lin_num

        self.step_lst.append(new_step)
        prin_lst(self.step_lst)

if( __name__ == "__main__"):
    uni_contr = controler()
    for times in xrange(5):
        command = str(raw_input(">>>"))
        uni_contr(command)
