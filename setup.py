#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    version='0.1.0',
    name='my-package',
    license='MIT License',
    description='',
    author='Firstname Lastname',
    author_email='my.email@protonmail.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'my-package=my_package.__main__:main',
        ],
    },

    python_requires='>=3.6.0',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=open("requirements.txt", "r").readlines(),
    tests_require=['pytest==5.2.0'],
    setup_requires=['pytest-runner'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ]
)
