def hi_msg():
    print "Hi there"

from deps.hi_deps import new_hi_msg
if(__name__ == "__main__"):
    hi_msg()
    new_hi_msg()
