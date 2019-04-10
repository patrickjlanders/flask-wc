#!/usr/bin/env python
from setuptools import setup, find_packages
setup(name='flask-by-example',
      version='1.0',
      packages=find_packages(),
      scripts=['manage.py']   # puts manage.py on PATH of virtualenv, so can run manage.py runserver from anywhere
      )
