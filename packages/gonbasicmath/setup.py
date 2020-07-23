#!/usr/bin/env python

from setuptools import setup


# This setup is suitable for "python setup.py develop".

setup(name='gonbasicmath',
      version='0.1',
      description='A silly math package',
      author='Gonzalo Amadio',
      author_email='gonzalo@mymath.org',
      url='http://www.mymath.org/',
      packages=['gonbasicmath', 'gonbasicmath.adv'],
      )


# REF:  https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html

# └─ $ ▶ sudo python setup.py develop
# [sudo] password for gamadio:
# running develop
# running egg_info
# creating gonbasicmath.egg-info
# writing gonbasicmath.egg-info/PKG-INFO
# writing top-level names to gonbasicmath.egg-info/top_level.txt
# writing dependency_links to gonbasicmath.egg-info/dependency_links.txt
# writing manifest file 'gonbasicmath.egg-info/SOURCES.txt'
# reading manifest file 'gonbasicmath.egg-info/SOURCES.txt'
# writing manifest file 'gonbasicmath.egg-info/SOURCES.txt'
# running build_ext
# Creating /usr/local/lib/python2.7/dist-packages/gonbasicmath.egg-link (link to .)
# Adding gonbasicmath 0.1 to easy-install.pth file
#
# Installed /home/gamadio/Playground/tests/packages/gonbasicmath
# Processing dependencies for gonbasicmath==0.1
# Finished processing dependencies for gonbasicmath==0.1

# This will install a link file in the site-packages folder that points to
# where ever your package resides. This is great for testing without actually
# installing your package.


# └─ $ ▶ python
# Python 3.6.9 (default, Apr 18 2020, 01:56:04)
# >>> import gonbasicmath
# >>> gonbasicmath.add(2,2)
# 4

