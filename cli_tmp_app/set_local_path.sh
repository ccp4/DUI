echo "This script should be run with the source command from ... /cli_tmp_app/ directory"
echo "setting up tmp path"
export PATH=$PATH:$(pwd)
export DUI_PATH=$(pwd)
cd $DUI_PATH/../dui/resources
echo "preparing phil parameter editor"
rm *.pyc
dials.python phil_edit_code_generator.py
cd $DUI_PATH
echo "done"
echo ""
echo "type \"run_DUI.sh\" (without quotes) to launch Dials User Interface"
echo ""
