echo "This script should be run with the source command from ... /cli_tmp_app/ directory"
echo "setting up tmp path"
export PATH=$PATH:$(pwd)
export DUI_PATH=$(pwd)
cd $DUI_PATH/../dui/resources
echo "preparing phil parameter editor"
rm *.pyc
#dials.python phil_edit_code_generator.py #only needed for the old DUI
cd $DUI_PATH
echo "DUI_PATH =$(pwd)"
cd ../idials_GUI/
export IDIALS_PATH=$(pwd)
echo "done"
echo ""
echo "type \"run_DUI.sh\" (without quotes) to launch Dials User Interface"
echo ""
echo "type \"idials_GUI.sh\" (without quotes) to launch iDIALS GUI"
echo ""
echo "type \"img_view.sh\" (without quotes) to launch IMG PyQt4 viewer"
echo "IDIALS_PATH=$IDIALS_PATH"
cd $DUI_PATH
