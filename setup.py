#!/usr/bin/env python

from setuptools import setup, find_packages

desc = ''
with open('README.rst') as f:
    desc = f.read()

setup(
    name='wheelify',
    version='0.1.4',
    description=('Simple manylinux wheel builder utility'),
    long_description=desc,
    url='https://github.com/jmvrbanac/wheelify',
    author='John Vrbanac',
    author_email='john.vrbanac@linux.com',
    license='Apache v2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='manylinux wheel builder',
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    install_requires=[],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
            'wheelify = wheelify.app:main'
        ],
    },
)
