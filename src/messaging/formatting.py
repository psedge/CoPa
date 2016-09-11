import socket
import struct
import random

from messaging.transport import Handler, TransportMethod
from util.exceptions import TransportException, PackingException


class Message(object):

    def __init__(self, message, args={}):
        self.raw = message

    def send(self, transport_class):
        """
        Send the message via the provided transport method.

        :param transport_class:
        :return:
        """
        return False
        parts = Pakcer.split(data=str(self), size=64)

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

    @staticmethod
    def pad(data, length):
        if not isinstance(data, bytearray):
            raise PackingException('Data provided not instance of a byte array.')

        while len(data) < length:
            data.extend(b' ')
        return data

    @staticmethod
    def split(data, byte_size=64):
        """
        Should be interesting to see how far we get with this

        :param data:
        :param byte_size:
        :return:
        """

        if not isinstance(byte_size, int):
            raise Exception('Byte length not integeric')

        parts = []
        current_part = bytearray()

        for i in range(0, len(data.encode())):
            current_part.extend(data[i].encode())
            if len(bytes(current_part)) == byte_size:
                parts.append(current_part)
                current_part = bytearray()

        if len(bytes(current_part)) != 0:
            Packer.pad(current_part, byte_size)
            parts.append(current_part)

        return parts
