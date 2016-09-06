import os
import sys

import time

from gui.window import Window
from util.manager import Manager
from multiprocessing import Process, Queue

"""
This is the summer of our discontent made glorious by example messages

Initiate CoPa. Start the GUI and await connections.
"""

if not os.geteuid() == 0:
    exit("\n Needs to be run as root user. \n")

q = Queue()

w = Window(queue=q)
gui = Process(name='gui', target=w(), args=()).start()

while True:
    while q.empty():
        time.sleep(1)

    print(q.get())

# manager = Manager()
# manager.process_input(gui.join())

sys.exit(0)
