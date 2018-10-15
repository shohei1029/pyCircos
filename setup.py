#!/usr/bin/env python3

from setuptools import setup, find_packages
 
setup(
    name             = 'pyCircos',
    version          = '1.0.0.dev0',
    description      = 'Python Circos created by @ponnhide.',
     #license          = __license__,
    author           = 'S.N.',
    author_email     = '',
    url              = 'https://github.com/shohei1029/pyCircos.git',
    keywords         = 'bioinformatics',
    packages         = find_packages(),
    python_requires  = '>=3',
    install_requires = [
        'biopython',
        'matplotlib',
        ],
)
