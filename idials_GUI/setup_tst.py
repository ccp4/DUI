from distutils.core import setup
setup(name='tst_01',
      py_modules=['python_qt_bind',
                  'custom_widgets',
                  'dynamic_reindex_gui',
                  'idials_gui',
                  'outputs_gui',
                  'idials_main_widget',
                  'simpler_param_widgets',
                  'outputs_n_viewers.compyling_boost_ext',
                  'outputs_n_viewers.img_viewer',
                  'outputs_n_viewers.img_view_tools',
                  'outputs_n_viewers.info_handler',
                  'outputs_n_viewers.web_page_view',
                  'params_live_gui_generator'],
      data_files=[('logos', ['resources/DIALS_Logo_smaller_centred.png',
                   'resources/export.png', 'resources/find_spots.png',
                   'resources/import.png', 'resources/index.png',
                   'resources/integrate.png', 'resources/refine.png',
                   'resources/refine_v_sets.png',
                   'resources/reindex.png'])]
      version='1.0',
      description='test with python source files only',
      author='Luiso',
      author_email='luis.fuentes-montero@diamond.ac.uk',
     )

bkp = '''
'resources/DIALS_Logo_smaller_centred.png', 'resources/export.png',
'resources/find_spots.png', 'resources/import.png', 'resources/index.png',
'resources/integrate.png', 'resources/refine.png',
'resources/refine_v_sets.png', 'resources/reindex.png',
'''
