import sys

from gui import Gui
from src.debug import Debug
from socket_handler import SocketHandler
from encr import Encryption
from hash import Hash
from pack import Packer

class CoPa:
    log = None
    gui = None
    _messages = []
    _socket = None
    _config = {"addr": None}

    PACKET_LENGTH = 64

    def __init__(self):
        self.log = Debug()
        callback = getattr(self, 'send_message')
        config_callback = getattr(self, 'do_action')
        self._wait_for_connections(callback)
        self.gui = Gui(self.log, lambda x: callback(x), lambda x, y: config_callback(x, y))

    def _wait_for_connections(self, callback):
        callback = getattr(self, 'new_connection')
        self._socket = SocketHandler(self.log, lambda x: callback(x))
        self.log.write('Waiting for connections', 'DEBUG')

    def do_action(self, action, params):
        if action == 'connect':
            self._config['addr'] = params['addr']
            self.log.write('Connecting to ' + params['addr'], 'DEBUG')

    def new_connection(self, data, addr):
        message = Encryption.decrypt_data(data)

        self.gui.receive(message, addr)

    def send_message(self, message):
        if self._config['addr'] is None:
            return

        data = Hash.create_message_object(message)

        self._messages.append(data)

        for part in Packer.split(message['message'], self.PACKET_LENGTH):

            crypto = Encryption(part)
            encrypted_data = crypto.encrypt_data()

            self._socket.post_connection(encrypted_data, self._config['addr'])

"""
This is the summer of our discontent made glorious by example messages

Initiate CoPa. Start the GUI and await connections.

"""
copa = CoPa()

sys.exit(0)