# launching test mini idials toy
MY_WD=$(cd $(dirname ${0}); pwd)
#echo "MY_WD= $MY_WD"
dials.python $MY_WD/m_idials_gui.py
