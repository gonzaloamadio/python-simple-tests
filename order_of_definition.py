# Can we declare a class after it is used?

class A():
    def ppp(self):
        print("Appp")
        B.pppb()

class B():
    @classmethod
    def pppb(cls):
        print("Bppp")

x = A()
x.ppp()
