# setup script to prepare setpath script

# Python script the generates setpath.sh script
# with hard-codded path to runnable tools
MY_WD = $(pwd)
dials.python write_setpath.py $MY_WD

# making runnable the setpath script
chmod +x setpath.sh

#Attemplting to compile list C++ extension
cd ../idials_GUI/outputs_n_viewers
dials.python compyling_boost_ext.py
cd $MY_WD
