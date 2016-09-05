import unittest

from messaging.formatting import Packer


class PackingTest(unittest.TestCase):

    def test_pack(self):
        """
        Test that packing data to a certain size works.
        :return:
        """
        size = 32
        parts = Packer.split("a" * 128, size)
        self.assertEqual(len(parts), 4)

        for part in parts:
            self.assertEquals(len(part), size)

    def test_pad(self):
        """
        Test that padding works.

        :return:
        """
        size = 64
        data = Packer.pad(bytearray(), size)
        self.assertEquals(len(data), size)
