import os

import sys

import settings

from gui.gui import Window
from messaging.pack import Packer
from messaging.socket_handler import SocketHandler
from security.encr import Encryption
from security.hash import Hash
from util.debug import Debug

"""
This is the summer of our discontent made glorious by example messages

Initiate CoPa. Start the GUI and await connections.
"""

if not os.geteuid() == 0:
    exit("\n Needs to be run as root user. \n")

log = Debug()
messages = []
config = {"addr": None}


def do_action(action, params):
    if action == 'connect':
        config['addr'] = params['addr']
        log.write('Connecting to ' + params['addr'], 'DEBUG')
        return 'Connecting to ' + params['addr']


def send_message(message):
    if config['addr'] is None:
        return


Window(
        log,
        lambda x: send_message(x),
        lambda x, y: do_action(x, y)
    )


sys.exit(0)
