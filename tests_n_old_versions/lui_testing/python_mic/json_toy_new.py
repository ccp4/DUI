import json

class MyClass:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self): #overridding this to return tuples of (key,value)
        return iter([('x',self.x),('y',self.y),('z',self.z)])


a1 = MyClass(2,"tres",4.0)

tst = dict(a1)

with open('data.json', 'w') as outfile:
    json.dump(tst, outfile)
