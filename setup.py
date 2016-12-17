#!/usr/bin/env python

from distutils.core import setup

setup(
    name             = 'ingest',
    version          = '0.1.0',
    description      = 'LiveStories Data transformation',
    long_description = 'Transform various data types to LiveStories format',
    author           = 'Dan Lecocq',
    author_email     = 'sowiebinich@gmail.com',
    url              = 'http://github.com/livestories/ingest-test',
    license          = 'MIT',
    platforms        = 'Posix; MacOS X',
    classifiers      = [
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP'
    ],
    packages         = [
        'ingest'
    ],
    package_dir      = {
        'ingest': 'ingest'
    },
    install_requires = [
        'six'
    ],
    tests_require    = [
        'coverage',
        'nose',
        'rednose',
    ],
    **kwargs
)
