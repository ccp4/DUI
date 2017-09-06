import json
class UniStep(object):
    def __init__(self):
        self.lin_num = 0
        self.next_step_list = None
        self.command_lst = [None]
        self.success = None
        self.pickle_file_out = None
        self.json_file_out = None
        self.phil_file_out = None
        self.report_out = None

        tmp_off = '''
        self.prev_step = prev_step
        self.dials_comand = DialsCommand()
        self.work_dir = os.getcwd()
        '''
class MyClass:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self): #overridding this to return tuples of (key,value)
        return iter([('x',self.x),('y',self.y),('z',self.z)])


a1 = MyClass(1,2,3)

tst = dict(a1)

with open('data.json', 'w') as outfile:
    json.dump(tst, outfile)
