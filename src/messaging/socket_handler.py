import sys
from socket import socket, AF_INET, SOCK_RAW, IPPROTO_ICMP, SOL_IP, IP_HDRINCL


class SocketHandler:
    _socket = None

    def __init__(self, log, callback):
        self.callback = callback
        self.dbg = log

        self._socket = socket(
            family=AF_INET,
            type=SOCK_RAW,
            proto=IPPROTO_ICMP)

        self._socket.setsockopt(SOL_IP, IP_HDRINCL, 1)

    def receive_connection(self):
        while True:
            data, addr = self._socket.recvfrom(1508)
            self.callback(data, addr)
            self.dbg.write("Packet from %r: %r" % (addr, data))

    def post_connection(self, message, addr):
        while self.wait_for_confirmation(hash):
            packet = IMCP()
            packet.message = message

            print(packet.prepare())
            sys.exit()
            self._socket.send(packet.prepare())

    def wait_for_confirmation(self, hash):
        return False
