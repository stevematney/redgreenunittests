# -*- coding: utf-8 -*-
#!/usr/bin/env python

from setuptools import setup


version = "0.1.1"
readme = open('README.md').read()

setup(
    name='redgreenunittest',
    version=version,
    description='This is literally an exact clone of unittest (from Python 2.7), but with colors.',
    long_description=readme,
    author='Steve Matney',
    url='https://github.com/stevematney/redgreenunittests',
    packages=[
        'redgreenunittest',
        'redgreenunittest.django'
    ],
    install_requires=[
        'Pygments',
    ]
)
