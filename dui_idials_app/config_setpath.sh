# setup script to prepare setpath script

# Python script the generates setpath.sh script
# with hard-codded path to runnable tools
dials.python write_setpath.py $(pwd)

# making runnable the setpath script
chmod +x setpath.sh
