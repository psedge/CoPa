import sys
import socket
import struct
import random


"""
Most of this is derived, nicked, nabbed, stolen, taken, borrowed, and just outright-ripped-off from @pklaus, from his original implementation of ping.c in python.
If you ever read this, thank you for saving me many hours of my life.
"""
class IMCP:

    message = ''
    ICMP_ECHO_REQUEST = 8 # Seems to be the same on Solaris.
    ICMP_CODE = socket.getprotobyname('icmp')

    def prepare(self):
        packet_id = int((id(1) * random.random()) % 65535)

        # Header is type (8), code (8), checksum (16), id (16), sequence (16)
        header = struct.pack('bbHHh', self.ICMP_ECHO_REQUEST, 0, 0, packet_id, 1)
        data = 192 * 'Q'

        # Calculate the checksum on the data and the dummy header.
        my_checksum = self.checksum(header + data)
        # Now that we have the right checksum, we put that in. It's just easier
        # to make up a new header than to stuff it into the dummy.
        header = struct.pack('bbHHh', self.ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), packet_id, 1)

        return header + data

    def checksum(self, source_string):
        # I'm not too confident that this is right but testing seems to
        # suggest that it gives the same answers as in_cksum in ping.c.
        sum = 0
        count_to = (len(source_string) / 2) * 2
        count = 0

        while count < count_to:
            this_val = ord(source_string[count + 1])*256+ord(source_string[count])
            sum += this_val
            sum &= 0xffffffff # Necessary?
            count += 2
        if count_to < len(source_string):
            sum += ord(source_string[len(source_string) - 1])
            sum = sum & 0xffffffff # Necessary?
        sum = (sum >> 16) + (sum & 0xffff)
        sum = sum + (sum >> 16)
        answer = ~sum
        answer = answer & 0xffff

        # Swap bytes. Bugger me if I know why.
        answer = answer >> 8 | (answer << 8 & 0xff00)
        return answer