#coding=utf-8
from setuptools import setup
import PFetion

setup(
    name = PFetion.__name__,
    version = PFetion.__version__,
    packages = ['PFetion'],
    keywords = 'library mobile fetion',
    author = PFetion.__author__,
    author_email = 'whtsky@gmail.com',

    url = PFetion.__website__,
    description = 'A simple python lib for WapFetion',
    long_description = open("README.md").read(),
    license = PFetion.__license__,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    zip_safe = False,
)

