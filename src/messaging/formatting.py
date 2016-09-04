import socket
import struct
import random

from messaging.transport import Handler, TransportMethod
from util.exceptions import TransportException


class Message(object):

    def __init__(self, message, args={}):
        self.raw = message

    def send(self, transport_class):
        """
        Send the message via the provided transport method.

        :param transport_class:
        :return:
        """
        packer = Packer(size=64)
        parts = packer.split(str(self))

        try:
            if not isinstance(transport_class, TransportMethod):
                raise TransportException("Transport Class provided is not a child of TransportMethod.")

            transport = Handler(transport_class)

            for part in parts:
                transport.send(part)
        except TransportException:
            return False

    def __str__(self):
        return str(self.raw)


class Packer:
    """
    Split the message into a number of packets.
    """
    def __init__(self, size=64):
        if not isinstance(size, int):
            raise Exception('byte length not integeric')
        self.byte_size = size

    @staticmethod
    def pad(data, length):
        while len(data) < length:
            data.extend(b' ')
        return data

    def split(self, data):
        """
        Should be interesting to see how far we get with this

        :param data:
        :return:
        """
        parts = []
        current_part = bytearray()

        for i in range(0, len(bytes(data.encode())) - 1):
            current_part.extend(data[i].encode())
            if len(bytes(current_part)) == self.byte_size:
                parts.append(current_part)
                current_part = bytearray()

        if len(bytes(current_part)) < self.byte_size:
            self.pad(current_part, self.byte_size)

            parts.append(current_part)

        return parts
