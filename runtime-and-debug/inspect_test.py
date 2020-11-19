import inspect

class MyClass:
    """ A class """

    def __init__(self):
        pass

    def fun1(self, a, b):
        return 0

    def fun2(self):
        return 1

def myfunc():

    # frame demo
    currentframe = inspect.currentframe()
    callgraph=inspect.getouterframes(currentframe)

    print('Call Graph for {0:s}'.format(myfunc.__name__))
    for record in callgraph:
        frameinfo = inspect.getframeinfo(record[0])
        print(frameinfo.function)


# Simple generator returning fibonacci numbers

def mygen():
    a = 0
    b = 1
    while True:
        c = a+b
        yield c
        a,b = b,c
