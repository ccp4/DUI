
class anything(object):

    def call_me(self):

        def test1(var1):
            print "from test1"
            print "var1 =", var1
        print "after def test1"
        test1(5)

if( __name__ == "__main__" ):
    print "Hi"

    a = anything()
    a.call_me()

    print "Hi 2"


