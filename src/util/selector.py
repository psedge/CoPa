from util.commands import *
from util.exceptions import CommandException


class Selector:
    gui = None
    commands = {
        'help': Help,
        'connect': Connect,
        'clear': Clear,
        'exit': Exit,
    }

    def __init__(self, string, params=[]):
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

    def execute(self):
        return self.command.execute()