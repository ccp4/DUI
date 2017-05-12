echo "files BEFORE testing setup"
echo " "
ls
echo " "
echo "Testing setup.py with sdist command"
echo " "
python setup.py sdist
echo " "
echo "listing AFTER setup test"
echo " "
ls
