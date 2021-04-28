#!usr/bin/env python

from setuptools import setup
from setuptools import find_packages

setup(
    name='qCalc',
    version='1.0',
    description='Simple calculator project',
    author='IVS-DREAM-TEAM',
    author_email='xgajdo30@stud.fit.vutbr.cz',
    url='https://github.com/HasicJoe/IVS-DREAM-TEAM',
    py_modules=['main','lib.eventhandler', 'lib.mathlib', 'lib.profiler', 'gui.gui', 'tests'],
    tests_require=['pytest'],
    install_requires=['PyQt5', 'cProfiler'],
)