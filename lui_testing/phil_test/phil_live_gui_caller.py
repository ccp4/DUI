
from phil_live_gui_generator import tmp_main

if __name__ == '__main__':

    '''
    from python_qt_bind import GuiBinding
    gui_lib = GuiBinding()
    print "using ", gui_lib.pyhon_binding
    qt_tool = gui_lib.pyhon_binding
    '''
    #TODO uncomment previous code and make it work
    qt_tool = "PyQt4"


    lst_phl_obj = []

    from dials.command_line.find_spots import phil_scope as phil_scope_find_spots
    lst_phl_obj.append(phil_scope_find_spots)
    from dials.command_line.index import phil_scope as phil_scope_index
    lst_phl_obj.append(phil_scope_index)
    from dials.command_line.refine import phil_scope as phil_scope_refine
    lst_phl_obj.append(phil_scope_refine)
    from dials.command_line.integrate import phil_scope as phil_scope_integrate
    lst_phl_obj.append(phil_scope_integrate)

    try:
        from dials.command_line.export import phil_scope as phil_scope_export
    except:
        from dials.command_line.export_mtz import phil_scope as phil_scope_export

    lst_phl_obj.append(phil_scope_export)

    lst_pos = 3
    tmp_main(lst_phl_obj[lst_pos])
