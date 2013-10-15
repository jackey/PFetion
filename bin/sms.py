#!/usr/bin/env python
import sys,os

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(APP_PATH);

from PFetion import Fetion

fetion = Fetion('15821121753', 'lovexx1314')

fetion.send(sys.argv[1], sys.argv[2])
