import time
import hashlib
import sys

from Crypto.Cipher import Blowfish
from skein import threefish


class Encryption:
    __keys = False
    __tweak = False
    _data = None

    def __init__(self, data):
        self._data = data
        self.__keys = False
        self.__tweak = False

    def _check_self(self):
        if self.__keys == False:
            with open("/dev/urandom", 'rb') as file:
                self.__keys = file.read(64)

        if self.__tweak == False:
            with open("/dev/urandom", 'rb') as file:
                self.__tweak = file.read(16)

        if self._data == None:
            raise Exception('No data')

        return True

    def decrypt_data(self):
        self._data = self._decrypt()
        self._check_self()

        return self._data

    def encrypt_data(self):
        if (self._check_self()):
            message = self._data
            self._data = self._encrypt(message)

            return self._data

    def _encrypt(self, message):
        tf = threefish(self.__keys, self.__tweak)

        return tf.encrypt_block(bytes(message))


