#!/usr/bin/env python

from setuptools import setup, find_packages
 
setup(
    name             = 'pyCircos',
    version          = '1.0.0.dev2',
    description      = 'Python Circos created by @ponnhide.',
     #license          = __license__,
    author           = 'S.N. and ponnhide',
    author_email     = '',
    url              = 'https://github.com/shohei1029/pyCircos.git',
    keywords         = 'bioinformatics',
    packages         = find_packages(),
    python_requires  = '>=2.7.13, >=3.6.2',
    install_requires = [
        'biopython',
        'matplotlib>=2.0.0',
        ],
)
