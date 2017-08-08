# launching test mini idials toy
MY_WD=$(cd $(dirname ${0}); pwd)
export BOOST_ADAPTBX_FPE_DEFAULT=1
export BOOST_ADAPTBX_SIGNALS_DEFAULT=1
export IDIALS_GUI_PATH=$MY_WD
dials.python $MY_WD/m_idials_gui.py
