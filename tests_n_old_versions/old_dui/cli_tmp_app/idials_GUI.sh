echo "Running DUI from local copy of bzr repo"
export BOOST_ADAPTBX_SIGNALS_DEFAULT=1
export BOOST_ADAPTBX_FPE_DEFAULT=1
dials.python $DUI_PATH/../idials_GUI/idials_gui.py
