import random
import struct
import sys
from socket import socket as sock, AF_INET, SOCK_RAW, IPPROTO_ICMP, SOL_IP, IP_HDRINCL, socket

from util.exceptions import TransportMethodException


class Handler:

    def __init__(self, transport_class):
        self.transport = transport_class

    # def receive_connection(self):
    #     while True:
    #         data, addr = self.transport._socket.recvfrom(1508)
    #         self.callback(data, addr)
    #         Debug.write("Packet from %r: %r" % (addr, data))

    def send(self, part, addr):
        packet = self.transport(part)
        print(packet.make_packet())
        sys.exit()


class TransportMethod:

    def __init__(self, message):
        self.message = message

        if not getattr(self, 'make_packet'):
            raise TransportMethodException("TransportMethod does not implement a make_packet() function.")


class IMCP(TransportMethod):
    """
    Most of this is derived, nicked, nabbed, stolen, taken, borrowed, and just outright-ripped-off from @pklaus, from his original implementation of ping.c in python.
    If you ever read this, thank you for saving me many hours of my life.
    """

    ICMP_ECHO_REQUEST = 8

    _socket = None

    def __init__(self, message):
        super(IMCP, self).__init__(message)

        self._socket = sock(
            family=AF_INET,
            type=SOCK_RAW,
            proto=IPPROTO_ICMP)

        self._socket.setsockopt(SOL_IP, IP_HDRINCL, 1)

    def make_packet(self):
        packet_id = int((id(1) * random.random()) % 65535)

        # Header is type (8), code (8), checksum (16), id (16), sequence (16)
        header = str(struct.pack('bbHHh', self.ICMP_ECHO_REQUEST, 0, 0, packet_id, 1))
        data = str(self.message)

        # Calculate the checksum on the data and the dummy header.
        my_checksum = self._checksum(header + data)
        # Now that we have the right checksum, we put that in. It's just easier
        # to make up a new header than to stuff it into the dummy.
        header = str(struct.pack('bbHHh', self.ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), packet_id, 1))

        return header + data

    @staticmethod
    def _checksum(source_string):
        # I'm not too confident that this is right but testing seems to
        # suggest that it gives the same answers as in_cksum in ping.c.
        sum = 0
        count_to = len(source_string) - 1
        count = 0

        while count < count_to:
            this_val = ord(source_string[count + 1]) * 256 + ord(source_string[count])
            sum += this_val
            sum &= 0xffffffff  # Necessary?
            count += 2

        if count_to < len(source_string):
            sum += ord(source_string[len(source_string) - 1])
            sum = sum & 0xffffffff  # Necessary?

        sum = (sum >> 16) + (sum & 0xffff)
        sum = sum + (sum >> 16)
        answer = ~sum
        answer = answer & 0xffff
        # Swap bytes. Bugger me if I know why.
        answer = answer >> 8 | (answer << 8 & 0xff00)
        return answer
