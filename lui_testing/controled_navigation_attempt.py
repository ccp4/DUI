def dummy_reminder():

    '''
    This is the first attempt to find the allowed next step to run with iDIALS
    '''

    #print "dir(self.idials_widget.controller) =", dir(self.idials_widget.controller)
    dir_controler = '''
    ['get_command_tree', 'get_current', 'get_history', 'get_mode', 'get_models', 'get_parameters', 'get_report'
    , 'get_summary', 'goto', 'lock', 'mode_list', 'redo_parameters', 'reset_parameters', 'run', 'set_mode'
    , 'set_parameters', 'state', 'state_filename', 'undo_parameters']
    '''
    #print "mode_list =", self.idials_widget.controller.mode_list
    #print "get_models=", self.idials_widget.controller.get_models()

    curr = self.idials_widget.controller.get_current()
    dir_curr = '''
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__',
    '__iter__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
    '__str__', '__subclasshook__', '__weakref__', 'applied', 'as_dict', 'children', 'description', 'directory',
    'experiments', 'from_dict', 'index', 'name', 'output', 'parameters', 'parent', 'reflections', 'report',
    'success', 'workspace']
    '''
    curr_mode = self.idials_widget.controller.get_mode()
    print "curr_mode =", curr_mode
    #curr_loc = self.idials_widget.controller.lock
    #print "dir(curr_loc) =", dir(curr_loc)

    print "curr.children =", curr.children
    print "curr.parent =", curr.parent

    print "curr.workspace =", curr.workspace
    #find allowed_parents

    #print "dir(self.idials_widget.controller) =", dir(self.idials_widget.controller)
    dir_controler = '''
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__',
    '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    '__weakref__', 'get_command_tree', 'get_current', 'get_history', 'get_mode', 'get_models', 'get_parameters',
    'get_report', 'get_summary', 'goto', 'lock', 'mode_list', 'redo_parameters', 'reset_parameters', 'run', 'set_mode',
    'set_parameters', 'state', 'state_filename', 'undo_parameters']
    '''
    print "self.idials_widget.controller.state =", self.idials_widget.controller.state

    curr_state = self.idials_widget.controller.state
    dir_curr_state = '''
    ['CommandClass', 'Memento', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__',
    '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
    '__str__', '__subclasshook__', '__weakref__', 'as_dict', 'command_tree', 'counter', 'current', 'dump', 'from_dict', 'goto',
    'load', 'mode', 'parameters', 'run', 'workspace']
    '''
    print "curr_state.mode =", curr_state.mode

    curr_run = self.idials_widget.controller
    print dir(curr_run)

