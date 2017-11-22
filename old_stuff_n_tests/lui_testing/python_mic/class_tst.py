class test(object):
    a = 5

    def __init__(self):
        print "a = ", self.a
    def __call__(self, new_a):
        self.a = new_a


if( __name__ == "__main__" ):
    x_obj = test()
    print "x_obj.a =", x_obj.a
    x_obj(9)
    print "x_obj.a =", x_obj.a
    y_obj = test()
    print "y_obj.a =", y_obj.a

