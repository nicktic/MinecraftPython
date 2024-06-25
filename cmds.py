import minescript
import sys
import time as t
from commands import infhealth, killall, portal


def god(gm):
    infhealth.godplr()

def closestPortal(prtl):
    portal.getportal()

gm = sys.argv[1]
prtl = sys.argv[2]

