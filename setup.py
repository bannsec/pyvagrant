# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os, sys, ast

here = os.path.abspath(os.path.dirname(__file__))
version = '0.2'

long_description = "See website for more info."

setup(
    name='pyvagrant',
    version=version,
    description='Python wrapper around Vagrant.',
    long_description=long_description,
    url='https://github.com/bannsec/pyvagrant',
    author='Michael Bann',
    author_email='self@bannsecurity.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Environment :: Console'
    ],
    keywords='vagrant',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['prettytable', 'prompt_toolkit', 'appdirs'],
    extras_require={
        'dev': ['ipython','twine','pytest','python-coveralls','coverage==4.5.4','pytest-cov','pytest-xdist','sphinxcontrib-napoleon', 'sphinx_rtd_theme','sphinx-autodoc-typehints', 'pyOpenSSL', 'numpy'],
    },
    entry_points={
        'console_scripts': [
            'vagrant-menu = vagrant_menu.menu:main',
        ],
    },
    include_package_data = True,
)

