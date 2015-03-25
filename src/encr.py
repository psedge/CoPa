import time
import hashlib
import sys


class Encryption:
    __keys = False
    _data = None

    def __init__(self, data):
        self._data = data
        self.__keys = '0987vfn098gy0982n7c'

    def _check_self(self):
        if self.__keys == False:
            raise Exception('No keys set')

        if self._data == None:
            raise Exception('No data to decrypt')

    def decrypt_data(self):
        self._check_self()

        return self._data

    def encrypt_data(self):
        self._check_self()

        return self._data