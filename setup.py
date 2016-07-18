#!/usr/bin/env python

import setuptools

from starter_api import info

setuptools.setup(
    name=info.__package_name__,
    version=info.__version__,
    author='Artur Geraschenko',
    author_email='arturgspb@gmail.com',
    description='Client for Starter Server API',
    description_file='README.rst',
    license='MIT',
    url='https://github.com/rw-meta/starter-py-client',
    setup_requires=['requests'],
    packages=["starter_api"],
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'starter_api': 'starter_api'},
    include_package_data=True,
)
