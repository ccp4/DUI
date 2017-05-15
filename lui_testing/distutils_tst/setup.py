from distutils.core import setup
setup(name='hi_tst',
      py_modules=['h_w', 'deps.hi_deps'],
      version='1.0',
      description='test with simple Hello w...',
      author='Luiso',
      author_email='luis.fuentes-montero@diamond.ac.uk',

      data_files=[('logos', ['logo_png/dials_logo_scaled.png', 'logo_png/dials_logo_scaled_gray.png'])]

     )
to_add_latter = '''
    url='https://www.python.org/sigs/distutils-sig/',
    packages=['distutils', 'distutils.command'],
    '''
