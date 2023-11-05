import unittest

def foo(x):
    if x == 1:
        raise ValueError('Wrong value!')
    return x


class TestExceptions(unittest.TestCase):

    def test_foo(self):

        print("assert foo(2) == 2")
        assert foo(2) == 2

        print("Test code reached after exception")
        with self.assertRaises(ValueError):
            flag = False
            foo(1)
            flag = True
            print("Is this reached?")

        print("Expected code was reached?: {}".format(flag))

if __name__ == '__main__':
    unittest.main()
