import socket
import sys

from src.imcp import IMCP


class SocketHandler:
    _socket = None

    def __init__(self, log, callback):
        self.callback = callback
        self.dbg = log

        self._socket = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
        self._socket.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)

    def receive_connection(self):
        while True:
            data, addr = self._socket.recvfrom(1508)
            self.callback(data, addr)
            self.dbg.write("Packet from %r: %r" % (addr,data))

    def post_connection(self, message, addr):
        while self.wait_for_confirmation(hash) == False:
            packet = IMCP()
            packet.message = message

            print(packet.prepare())
            sys.exit()
            self._socket.send(packet.prepare())

    def wait_for_confirmation(self, hash):
        return False
