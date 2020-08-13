class A():
  @staticmethod
  def foo():
    print("asd")


class B(A):
  def foo2(self):
    self.foo()

# >>> x = B()
# >>> x.foo2()
