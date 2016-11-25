import sys

def write_script(self_path):
    print "path =", self_path
    print "writing setpath.sh"

    lst_lin = []


    lst_lin.append( " echo \"This script should be run with the source command \"  ")
    lst_lin.append( " echo \"setting up tmp path\" ")

    line_w_path = " export DUI_PATH=\""
    line_w_path += self_path
    line_w_path += "\""
    lst_lin.append( line_w_path)


    lst_lin.append( " export PATH=$PATH:$DUI_PATH")
    lst_lin.append( " cd $DUI_PATH")
    lst_lin.append( " echo \"DUI_PATH =$DUI_PATH\"")
    lst_lin.append( " cd ../idials_GUI/")
    lst_lin.append( " export IDIALS_PATH=$DUI_PATH")
    lst_lin.append( " echo \"IDIALS_PATH=$IDIALS_PATH\"")
    lst_lin.append( " echo \"done\"")
    lst_lin.append( " echo \" \" ")
    lst_lin.append( " echo \"type  \"dui_idials\" (without quotes) to launch DUI/iDIALS\"\ ")
    lst_lin.append( " echo \" \" ")
    lst_lin.append( " cd $DUI_PATH")

    for lin in lst_lin:
        print lin



if( __name__ == "__main__" ):

    print "sys.argv =", sys.argv
    if( len(sys.argv) > 1 ):
        self_path = sys.argv[1]
        write_script(self_path)
    else:
        print "no path to connect provided"

    print "setpath.sh generated with the path: ", self_path
