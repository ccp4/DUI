echo "This script should be run with the source command from ... /cli_tmp_app/ directory"
echo "setting up tmp path"
export PATH=$PATH:$(pwd)
export DUI_PATH=$(pwd)
cd $DUI_PATH/../dui/resources
#echo "preparing phil parameter editor"
rm *.pyc
#dials.python phil_edit_code_generator.py #only needed for the old DUI
cd $DUI_PATH
echo "DUI_PATH =$(pwd)"
cd ../idials_GUI/
export IDIALS_PATH=$(pwd)
echo "IDIALS_PATH=$IDIALS_PATH"
echo "done"
echo ""
echo "type \"dui_idials\" (without quotes) to launch DUI/iDIALS"
echo ""
cd $DUI_PATH
