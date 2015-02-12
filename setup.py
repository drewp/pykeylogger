#!/usr/bin/env python

from distutils.core import setup

setup(name='pykeylogger',
      version='1.0',
      description='Keylogger for linux using xlib',
      author='Andrew Moffat',
      author_email='andrew@formconstantdance.org',
      url='https://github.com/amoffat/pykeylogger',
      packages=['pykeylogger'],
      package_dir={'pykeylogger': '.'},
      classifiers='License :: OSI Approved :: BSD License',
     )
