echo "setting up tmp path"
export PATH=$PATH:$(pwd)
export DUI_PATH=$(pwd)
cd $DUI_PATH/../dui/
echo "generating phil parameter editor"
dials.python phil_edit_code_generator.py
cd $DUI_PATH
echo "done"
