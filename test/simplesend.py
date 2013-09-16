import sys,os

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(APP_PATH);

from PyWapFetion import Fetion, send2self, send

to = "15821121753"
send2self("15821121753", "xxxx", "LiXiu, Ni kan dao le ma ?");
print "Sent Message To %s" %(to)