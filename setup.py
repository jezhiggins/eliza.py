#!/usr/bin/python

import sys

try:
    from distutils.core import setup
except:
    if sys.version[0] < 2:
        print "jabber.py requires at least python 2.0"
        print "Setup cannot continue."
        sys.exit(1)
    print "You appear not to have the Python distutils modules"
    print "installed. Setup cannot continue."
    print "You can manually install eliza.py by copying eliza.py"
    print "to your /python-libdir/site-packages directory."
    sys.exit(1)
    
setup(name="eliza.py",
      version="0.2",
      py_modules=["eliza"],
      description="Cheesy Eliza knock-off  ",
      author="Joe Strout, Jeff Epler and Jez Higgins",
      author_email="jez@jezuk.co.uk",
      url="http://www.jezuk.co.uk/eliza",
      license="BSD style"
      )






