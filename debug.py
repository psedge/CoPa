import os
import sys
import time


class Debug:
    _messages = {"print": [], "log": []}
    _level = 'DEBUG'

    DEBUG = 'DEBUG'
    PRODUCTION = 'PRODUCTION'
    ERROR = 'ERROR'

    def write(self, message, level):
        if level == 'DEBUG':
            message = str(time.time()) + ' - ' + message
        self._messages['print'].append(message)
        print(message)

    def log(self, message, level = 'DEBUG'):
        self._messages['log'].append(message)
        self._write_to_log(message)

    def _write_to_log(self, message):
        return