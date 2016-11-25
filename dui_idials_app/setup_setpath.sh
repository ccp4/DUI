# setup script to prepare setpath script

# Python script the generates setpath.sh script
# with hard-codded path to runnable tools
dials.python write_setpath.py $(pwd)

# making runnable the setpath script
chmod +x setpath.sh

#the next four lines need further testing before replacing $(pwd)
#echo "Hi "
#SCRIPT=`realpath $0`
#SCRIPTPATH=`dirname $SCRIPT`
#echo "SCRIPTPATH = $SCRIPTPATH"
