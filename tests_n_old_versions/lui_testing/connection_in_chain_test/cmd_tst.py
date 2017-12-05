import subprocess

simple_exampl = '''
command_lst[1] = ['import', 'template=/scratch/dui/dui_test/only_9_img/th_8_2_####.cbf']
command_lst[2] = ['find_spots', 'spotfinder.mp.nproc=4']
command_lst[3] = ['index']
command_lst[4] = ['refine_bravais_settings']
command_lst[5] = ['reindex', 'solution=9']
command_lst[6] = ['refine']
command_lst[7] = ['integrate', 'integration.mp.nproc=4']
command_lst[8] = ['export', 'mtz.hklout=hkl_out.mtz']
'''

original_looks = '''
full_cmd_lst[1] = ['dials.import', 'template=/scratch/dui/dui_test/only_9_img/th_8_2_####.cbf', 'output.datablock=1_datablock.json']
full_cmd_lst[2] = ['dials.find_spots', 'spotfinder.mp.nproc=4', 'input.datablock=1_datablock.json', 'output.datablock=2_datablock.json', 'output.reflections=2_reflections.pickle']
full_cmd_lst[3] = ['dials.index', 'input.datablock=2_datablock.json', 'input.reflections=2_reflections.pickle', 'output.experiments=3_experiments.json', 'output.reflections=3_reflections.pickle']
full_cmd_lst[4] = ['dials.refine_bravais_settings', 'input.experiments=3_experiments.json', 'input.reflections=3_reflections.pickle', 'output.prefix=lin_4_']
full_cmd_lst[5] = ['dials.reindex', 'input.reflections=3_reflections.pickle', 'change_of_basis_op=a,b,c', 'output.reflections=5_reflections.pickle']
full_cmd_lst[6] = ['dials.refine', 'input.experiments=lin_4_bravais_setting_9.json', 'input.reflections=5_reflections.pickle', 'output.experiments=6_experiments.json', 'output.reflections=6_reflections.pickle']
full_cmd_lst[7] = ['dials.integrate', 'integration.mp.nproc=4', 'input.experiments=6_experiments.json', 'input.reflections=6_reflections.pickle', 'output.experiments=7_experiments.json', 'output.reflections=7_reflections.pickle']
full_cmd_lst[8] = ['dials.export', 'mtz.hklout=hkl_out.mtz', '7_experiments.json', '7_reflections.pickle']
'''

def build_cmd():

    full_cmd_lst = []

    #full_cmd_lst.append(['dials.import', 'template=/scratch/dui/dui_test/only_9_img/th_8_2_####.cbf',

    full_cmd_lst.append(['dials.import', 'template=/home/lui/ccp4/dui_test/only_9_img/X4_wide_M1S4_2_####.cbf',
                         'output.datablock=dials_files/1_datablock.json',
                         'output.log=dials_files/1_import.log',
                         'output.debug_log=dials_files/1_import_debug.log'
                         ] )
    '''
                        ['dials.import',
                         'template=/home/lui/ccp4/dui_test/th_9_3_0588/th_9_3_####.cbf',
                         'output.datablock=dials_files/1_datablock.json',
                         'output.log=dials_files/1_import.log',
                         'output.debug_log=dials_files/1_import.debug.log']
    '''


    full_cmd_lst.append(['dials.find_spots', 'spotfinder.mp.nproc=4',
                         'input.datablock=dials_files/1_datablock.json',
                         'output.datablock=dials_files/2_datablock.json',
                         'output.reflections=dials_files/2_reflections.pickle',
                         'output.log=dials_files/2_find_spots.log',
                         'output.debug_log=dials_files/2_find_spots_debug.log'
                         ] )
    '''
                        ['dials.find_spots',
                         'spotfinder.mp.nproc=8',
                         'input.datablock=dials_files/1_datablock.json',
                         'output.datablock=dials_files/2_datablock.json',
                         'output.reflections=dials_files/2_reflections.pickle',
                         'output.log=dials_files/2_find_spots.log',
                         'output.debug_log=dials_files/2_find_spots.debug.log']

    '''

    full_cmd_lst.append(['dials.index',
                         'input.datablock=dials_files/2_datablock.json',
                         'input.reflections=dials_files/2_reflections.pickle',
                         'output.experiments=dials_files/3_experiments.json',
                         'output.reflections=dials_files/3_reflections.pickle',
                         'output.log=dials_files/3_index.log',
                         'output.debug_log=dials_files/3_index_debug.log'
                         ] )
    '''
                        ['dials.index',
                         'input.datablock=dials_files/2_datablock.json',
                         'input.reflections=dials_files/2_reflections.pickle',
                         'output.experiments=dials_files/3_experiments.json',
                         'output.reflections=dials_files/3_reflections.pickle',
                         'output.log=dials_files/3_index.log',
                         'output.debug_log=dials_files/3_index.debug.log']

    '''
    full_cmd_lst.append(['dials.refine_bravais_settings',
                         'input.experiments=dials_files/3_experiments.json',
                         'input.reflections=dials_files/3_reflections.pickle',
                         'output.prefix=lin_4_',
                         'output.directory=dials_files',
                         'output.log=dials_files/4_refine_bravais_settings.log',
                         'output.debug_log=dials_files/4_refine_bravais_settings_debug.log'
                         ] )
    '''
                        ['dials.refine_bravais_settings',
                         'input.experiments=dials_files/3_experiments.json',
                         'input.reflections=dials_files/3_reflections.pickle',
                         'output.prefix=lin_4_',
                         'output.directory=dials_files',
                         'output.log=dials_files/4_refine_bravais_settings.log',
                         'output.debug_log=dials_files/4_refine_bravais_settings.debug.log']

    '''
    full_cmd_lst.append(['dials.reindex',
                         'input.reflections=dials_files/3_reflections.pickle',
                         'change_of_basis_op=a,b,c',
                         'output.reflections=dials_files/5_reflections.pickle'
                         ] )
    '''
                        ['dials.reindex',
                         'input.reflections=dials_files/3_reflections.pickle',
                         'change_of_basis_op=a,b,c',
                         'output.reflections=dials_files/5_reflections.pickle']

    '''
    full_cmd_lst.append(['dials.refine',
                         'input.experiments=dials_files/lin_4_bravais_setting_9.json',
                         'input.reflections=dials_files/5_reflections.pickle',
                         'output.experiments=dials_files/6_experiments.json',
                         'output.reflections=dials_files/6_reflections.pickle',
                         'output.log=dials_files/6_refine.log',
                         'output.debug_log=dials_files/6_refine_debug.log'
                         ] )
    '''
                        ['dials.refine',
                         'input.experiments=dials_files/lin_4_bravais_setting_9.json',
                         'input.reflections=dials_files/5_reflections.pickle',
                         'output.experiments=dials_files/6_experiments.json',
                         'output.reflections=dials_files/6_reflections.pickle',
                         'output.log=dials_files/6_refine.log',
                         'output.debug_log=dials_files/6_refine.debug.log']

    '''
    full_cmd_lst.append(['dials.integrate',
                         'integration.mp.nproc=4',
                         'input.experiments=dials_files/6_experiments.json',
                         'input.reflections=dials_files/6_reflections.pickle',
                         'output.experiments=dials_files/7_experiments.json',
                         'output.reflections=dials_files/7_reflections.pickle',
                         'output.phil=dials_files/7_integrate.phil',
                         'output.log=dials_files/7_integrate.log',
                         'output.debug_log=dials_files/7_integrate_debug.log'
                         ] )
    '''
                        ['dials.integrate',
                         'integration.mp.nproc=8',
                         'input.experiments=dials_files/6_experiments.json',
                         'input.reflections=dials_files/6_reflections.pickle',
                         'output.experiments=dials_files/7_experiments.json',
                         'output.reflections=dials_files/7_reflections.pickle',
                         'output.phil=dials_files/7_integrate.phil',
                         'output.log=dials_files/7_integrate.log',
                         'output.debug_log=dials_files/7_integrate.debug.log']
    '''
    full_cmd_lst.append(['dials.export',
                         'mtz.hklout=hkl_out.mtz',
                         'dials_files/7_experiments.json',
                         'dials_files/7_reflections.pickle',
                         'output.log=dials_files/8_export.log',
                         'output.debug_log=dials_files/8_export_debug.log'
                         ] )
    '''
                        ['dials.export',
                         'mtz.hklout=hkl_out.mtz',
                         'dials_files/7_experiments.json',
                         'dials_files/7_reflections.pickle',
                         'output.log=dials_files/8_export.log',
                         'output.debug_log=dials_files/8_export.debug.log'] #### here
    '''


    '''
                        ['dials.import',
                         'template=/home/lui/ccp4/dui_test/th_9_3_0588/th_9_3_####.cbf',
                         'output.datablock=dials_files/1_datablock.json',
                         'output.log=dials_files/1_import.log',
                         'output.debug_log=dials_files/1_import.debug.log']

                        ['dials.find_spots',
                         'spotfinder.mp.nproc=8',
                         'input.datablock=dials_files/1_datablock.json',
                         'output.datablock=dials_files/2_datablock.json',
                         'output.reflections=dials_files/2_reflections.pickle',
                         'output.log=dials_files/2_find_spots.log',
                         'output.debug_log=dials_files/2_find_spots.debug.log']

                        ['dials.index',
                         'input.datablock=dials_files/2_datablock.json',
                         'input.reflections=dials_files/2_reflections.pickle',
                         'output.experiments=dials_files/3_experiments.json',
                         'output.reflections=dials_files/3_reflections.pickle',
                         'output.log=dials_files/3_index.log',
                         'output.debug_log=dials_files/3_index.debug.log']

                        ['dials.refine_bravais_settings',
                         'input.experiments=dials_files/3_experiments.json',
                         'input.reflections=dials_files/3_reflections.pickle',
                         'output.prefix=lin_4_',
                         'output.directory=dials_files',
                         'output.log=dials_files/4_refine_bravais_settings.log',
                         'output.debug_log=dials_files/4_refine_bravais_settings.debug.log']

                        ['dials.reindex',
                         'input.reflections=dials_files/3_reflections.pickle',
                         'change_of_basis_op=a,b,c',
                         'output.reflections=dials_files/5_reflections.pickle']

                        ['dials.refine',
                         'input.experiments=dials_files/lin_4_bravais_setting_9.json',
                         'input.reflections=dials_files/5_reflections.pickle',
                         'output.experiments=dials_files/6_experiments.json',
                         'output.reflections=dials_files/6_reflections.pickle',
                         'output.log=dials_files/6_refine.log',
                         'output.debug_log=dials_files/6_refine.debug.log']

                        ['dials.integrate',
                         'integration.mp.nproc=8',
                         'input.experiments=dials_files/6_experiments.json',
                         'input.reflections=dials_files/6_reflections.pickle',
                         'output.experiments=dials_files/7_experiments.json',
                         'output.reflections=dials_files/7_reflections.pickle',
                         'output.phil=dials_files/7_integrate.phil',
                         'output.log=dials_files/7_integrate.log',
                         'output.debug_log=dials_files/7_integrate.debug.log']

                        ['dials.export',
                         'mtz.hklout=hkl_out.mtz',
                         'dials_files/7_experiments.json',
                         'dials_files/7_reflections.pickle',
                         'output.log=dials_files/8_export.log',
                         'output.debug_log=dials_files/8_export.debug.log']
    '''


    return full_cmd_lst

if(__name__ == "__main__"):

    lst_of_lsts = build_cmd()

    for cmd_lin in lst_of_lsts:

        my_process = subprocess.Popen(cmd_lin,
                                      stdout = subprocess.PIPE,
                                      stderr = subprocess.STDOUT,
                                      bufsize = 1)

        for line in iter(my_process.stdout.readline, b''):
            single_line = line[0:len(line)-1]
            print single_line

        my_process.wait()
        my_process.stdout.close()
        if(my_process.poll() == 0):
            print "\n _________________________________________________________________________________________________________ succes on", cmd_lin, "\n"

        else:
            print "\n _________________________________________________________________________________________________________ failed on", cmd_lin, "\n"




