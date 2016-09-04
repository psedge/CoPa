import os
import sys

from gui.window import Window
from util.manager import Manager

"""
This is the summer of our discontent made glorious by example messages

Initiate CoPa. Start the GUI and await connections.
"""

if not os.geteuid() == 0:
    exit("\n Needs to be run as root user. \n")


def callback(gui, string):
    manager = Manager(gui)
    manager.process_input(string)

gui = Window(lambda x, y: callback(x, y))

sys.exit(0)
