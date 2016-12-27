#!/usr/bin/env python

import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='MFRC522-python',
    description='A small class to interface with the NFC reader Module MFRC522 on the Raspberry Pi',
    packages=['MFRC522'],
    dependency_links=['https://github.com/lthiery/SPI-Py.git@master#egg=SPI-Py'],
    long_description=read('README.md')
)