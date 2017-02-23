#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='reproducer',
    version='0.0.1',
    author='Martin Bukatovič',
    author_email='mbukatov@redhat.com',
    license='Apache 2.0',
    url='https://github.com/mbukatov/tox-sitepackages-reproducer',
    description='Reproducer for tox issue #461',
    packages=find_packages(exclude=['tests']),
    )
