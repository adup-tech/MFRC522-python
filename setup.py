#!/usr/bin/env python

import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='MFRC522-python',
    version='0.0.1',
    description='A small class to interface with the NFC reader Module MFRC522 on the Raspberry Pi',
    author='mxgxw',
    author_email='mxgxw@example.com',
    packages=['MFRC522'],
    dependency_links=['https://github.com/lthiery/SPI-Py.git@master'],
    long_description=read('README.md')
)