#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Mapping',
    version='1.0.1',

    author='Samson Paul',
    author_email='you@site.example',
    license='GPL v3 or later',
    install_requires = [
        'MediaDrop >= 0.10.3', # use whatever version you support
    ],

    namespace_packages = ['mediadropext'],
    # package_data is only for binary distributions ("bdist_egg") otherwise ("sdist")
    # MANIFEST.in is used. One of the arcane things in setuptools:
    # http://stackoverflow.com/a/14159430/138526
    package_data={
        'mediadropext.mapping': [
            'public/*',
            'templates/*',
            'migrations/*.mako',
        ],
    },
    packages=find_packages(),
    entry_points = {
        'mediadrop.plugin': [
            'mapping = mediadropext.mapping.mediadrop_plugin',
        ],
    }
)

