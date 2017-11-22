echo "files BEFORE testing setup"
echo " "
ls -al
echo " "
echo "Testing setup.py with sdist command"
echo " "
python setup.py sdist
echo " "
echo "listing AFTER setup test"
echo " "
ls -al
