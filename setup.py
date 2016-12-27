#!/usr/bin/env python

from distutils.core import setup

setup(name='MFRC522-python',
      version='1.0',
      description='A small class to interface with the NFC reader Module MFRC522 on the Raspberry Pi',
      author='mxgxw',
      author_email='mxgxw@example.com',
      dependency_links=['https://github.com/lthiery/SPI-Py.git@master']
     )