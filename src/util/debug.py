import time


class Debug:
    _level = 'DEBUG'

    DEBUG = 'DEBUG'
    PRODUCTION = 'PRODUCTION'
    ERROR = 'ERROR'

    @staticmethod
    def write(message, level):
        if level == 'DEBUG':
            message = str(time.time()) + ' - ' + message
        print(message)

    @staticmethod
    def log(message, level='DEBUG'):
        Debug._write_to_log("(" + level + ")" + str(time.time()) + ' - ' + message)

    @staticmethod
    def _write_to_log(self, message):
        pass
