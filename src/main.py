import os
import sys
import time
import multiprocessing as mp

from gui.window import Window
from settings import *
from util.manager import Manager


"""
This is the summer of our discontent made glorious by example messages

Initiate CoPa. Start the GUI and await connections.
"""

if not os.geteuid() == 0:
    exit("\n Needs to be run as root user. \n")

print("CoPa v" + VERSION)

if __name__ == '__main__':
    gui = Window(Manager())
    gui.open()