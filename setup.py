# Copyright Alan (AJ) Pryor, Jr. 2018

from setuptools import setup, find_packages

setup(name='flask_accepts',
      author='Alan "AJ" Pryor, Jr.',
      author_email='apryor6@gmail.com',
      version='0.1.7',
      description='Easy Flask input validation',
      ext_modules=[],
      packages=find_packages(),
      install_requires=['Flask-RESTful>=0.3.7'],
      )
