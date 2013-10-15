#coding=utf-8
from __future__ import with_statement

__name__ = 'PFetion'
__version__ = '0.9.4'
__author__ = 'whtsky'
__website__ = 'https://github.com/jackey/PFetion'
__license__ = 'MIT'

from Fetion import Fetion


def send2self(mobile, password, message):
    x = Fetion(mobile, password)
    x.send2self(message)


def send(mobile, password, to, message):
    x = Fetion(mobile, password)
    x.send(to, message)
