"""
(Nick) - Appears to be file to compile optional C++ extension?
         Potentially unused in normal runnning?
"""
from __future__ import absolute_import, division, print_function

from distutils import sysconfig
from subprocess import call as shell_call

obj_name = "lst_ext"
inc_path = sysconfig.get_python_inc()
logger.info("\n sysconfig.get_python_inc() =", inc_path)
for pos, single_shar in enumerate(inc_path):
    if single_shar == "/":
        cut_inc_path = inc_path[0:pos]

com_lin_01 = (
    "g++ -I" + inc_path + " -I" + cut_inc_path + " -fPIC -c " + obj_name + ".cpp"
)
logger.info("com_lin_01 =\n", com_lin_01)

lib_path = sysconfig.get_python_lib()
logger.info("\n sysconfig.get_python_lib() =", lib_path)
for pos, single_shar in enumerate(lib_path):
    if single_shar == "/":
        cut_lib_path = lib_path[0:pos]

for pos, single_shar in enumerate(cut_lib_path):
    if single_shar == "/":
        cut_cut_lib_path = cut_lib_path[0:pos]

com_lin_02 = (
    "g++ -shared "
    + obj_name
    + ".o -L"
    + cut_cut_lib_path
    + " -lboost_python -L"
    + cut_lib_path
    + "/config -lpython2.7 -o "
    + obj_name
    + ".so"
)

logger.info("\n Compiling line 1:")
logger.info("cmd =", com_lin_01)
err_msg_01 = shell_call(com_lin_01, shell=True)
logger.info("\n Compiling line 2:")
logger.info("cmd =", com_lin_02)
err_msg_02 = shell_call(com_lin_02, shell=True)
logger.info("\n done compiling")

if err_msg_01 != 0 or err_msg_02 != 0:
    logger.info("Failed to compile some C++ extensions ")
    logger.info("DUI will remain fully functional")
    logger.info("just navigation from one step to another")
    logger.info("might be slower")
