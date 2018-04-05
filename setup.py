# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Application_Server',
    version='0.2.0',
    description='A Python package for Application_Server',
    long_description=readme,
    author='Sheena Davitt, Alan Treanor, Thomas Anderson',
    author_email='thomas.anderson@ucdconnect.ie',
    url='https://github.com/atreanor/OnYourBike',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points = {
    'console_scripts': [
        'bikes_static=Application_Server.core:bikes_static',
        'bikes_dynamic=Application_Server.core:bikes_dynamic',
        'weather=Application_Server.core:weather',
    ],
    },
)