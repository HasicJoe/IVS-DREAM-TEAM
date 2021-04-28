#!usr/bin/env python
from setuptools import find_packages
from setuptools import setup

setup(
    name='Riders Poff Calc',
    version='193486724908700',
    description='Simple calculator project',
    author='IVS-DREAM-TEAM',
    author_email='xgajdo30@stud.fit.vutbr.cz',
    url='https://github.com/HasicJoe/IVS-DREAM-TEAM',
    packages=find_packages(where="src"),
    py_modules=['main','lib.eventhandler', 'lib.mathlib', 'lib.profiler', 'gui.gui', 'tests'],
    tests_require=['pytest'],
    install_requires=['PyQt5'],
    #entry_points={'console_scripts': ['calc=main:main']},

)