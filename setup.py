#!/usr/bin/env python

import sys

try:
    from setuptools import setup
except ImportError:
    # Described here : https://stackoverflow.com/questions/69858963/how-can-one-fully-replace-distutils-which-is-deprecated-in-3-10
    if sys.version_info < (3, 12):
        from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='piera',
    version='1.5.0',
    description='a python hiera parser and validator',
    long_description=readme + '\n\n',
    long_description_content_type="text/markdown",
    author='Andrei Zbikowski',
    author_email='andrei.zbikowski@gmail.com',
    maintainer='Martin Smith',
    maintainer_email='martin.smith@clear.bank',
    url='http://github.com/ClearBank/piera',
    packages=['piera'],
    package_data={"": ["README.md"]},
    package_dir={'piera': 'piera'},
    include_package_data=True,
    install_requires=['pyyaml'],
    license='Apache 2.0',
    zip_safe=False,
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
