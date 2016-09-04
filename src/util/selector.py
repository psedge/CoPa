
from util.commands import *
from util.exceptions import CommandException


class Selector:
    commands = {
        'help': Help,
        'connect': Connect,
        'clear': Clear,
    }
    requires_gui = ('clear',)

    def __init__(self, string, params={}, gui=None):
        """
        Convert the string into a Command instance.

        :param string:
        :param params:
        """
        if string not in self.commands.keys():
            raise CommandException("Command not recognised")

        if params:
            self.command = self.commands[string](params)
        else:
            self.command = self.commands[string]()

    def get_output(self):
        return self.command.get_message()