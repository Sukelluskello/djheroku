#!/usr/bin/env python
''' Setuptools installation script for Djheroku '''
from __future__ import with_statement

from setuptools import setup

requirements = ''
with open('requirements.txt') as req:
    requirements = req.read()

setup_requirements = ''
with open('requirements-test.txt') as reqset:
    setup_requirements = reqset.read()

setup(name='Djheroku',
      version='0.2',
      description='Some helper functionality for binding Heroku configuration to Django',
      author='Ferrix Hovi',
      author_email='ferrix+git@ferrix.fi',
      url='http://github.com/ferrix/djheroku/',
      packages=['djheroku'],
      install_requires=requirements,
      setup_requires=setup_requirements,
      )
