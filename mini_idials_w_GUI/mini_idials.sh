# launching test mini idials toy
MY_WD=$(cd $(dirname ${0}); pwd)
export BOOST_ADAPTBX_FPE_DEFAULT=1
export BOOST_ADAPTBX_SIGNALS_DEFAULT=1
dials.python $MY_WD/m_idials.py $1 $2
