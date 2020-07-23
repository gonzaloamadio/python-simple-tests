import os
print(__file__)
print(os.path.join(os.path.dirname(__file__), '..'))
print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.abspath(os.path.dirname(__file__)))
print(__name__)
print(os.path.join(os.path.dirname(__name__), '..'))
print(os.path.dirname(os.path.realpath(__name__)))
print(os.path.abspath(os.path.dirname(__name__)))
