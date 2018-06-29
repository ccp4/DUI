
class SysArgvData(object):
    '''
    Some data
    '''
    someting = False

sys_arg = SysArgvData()


class dumy_class(object):
    def __init__(self):
        print "Hi there"
        print "sys_arg.someting =", sys_arg.someting
