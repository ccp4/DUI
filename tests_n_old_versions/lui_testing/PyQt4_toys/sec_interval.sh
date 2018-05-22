#!/bin/bash
echo "start"
sleep 1
echo "second 1"
python prn10.py
sleep 1
echo "second 2"
python prn10.py
sleep 1
python crash.py
echo "second 3"
python prn10.py
sleep 1
echo "second 4"
python prn10.py
sleep 1
echo "second 5"
python prn10.py
sleep 1
echo "second 6"
python prn10.py
exit
