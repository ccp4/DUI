cmake_minimum_required(VERSION 2.8)
project(dui NONE)

install(
    FILES
        LICENSE
    DESTINATION
        licenses/License-dui
)

install(
    DIRECTORY
        src/dui
    DESTINATION
        lib/py2/site-packages
)

install(
    PROGRAMS
        bin/dui
    DESTINATION
        bin
)

