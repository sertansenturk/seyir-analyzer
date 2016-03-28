#!/usr/bin/env python

from setuptools import setup

setup(name='seyiranalyzer',
      version='1.1',
      author='Sertan Senturk',
      author_email='contact AT sertansenturk DOT com',
      license='agpl 3.0',
      description='Tools to analyse the seyir (melodic progression) of scores and audio recordings of makam music',
      url='http://sertansenturk.com',
      packages=['seyiranalyzer'],
      install_requires=[
          "numpy",
          "scipy",
          "matplotlib"
      ],
)
