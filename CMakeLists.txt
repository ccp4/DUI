cmake_minimum_required(VERSION 2.8)
project(dui NONE)

install(
    FILES
        LICENSE.txt
    DESTINATION
        licenses/License-dui
)

install(
    DIRECTORY
        mini_idials_w_GUI
    DESTINATION
        lib/py2/site-packages
)

install(
    PROGRAMS
        bin/dui
    DESTINATION
        bin
)

