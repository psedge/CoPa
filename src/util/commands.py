import sys

from util.exceptions import CommandException


class Command:
    def __init__(self, *args):
        if not getattr(self, 'get_message'):
            raise CommandException("Command does not implement a get_message() function.")

        if not getattr(self, 'execute'):
            raise CommandException("Command does not implement a execute() function.")


class Help(Command):

    def get_message(self):
        help_message = "CoPa - The (Co)py(Pa)ste Messaging Application.\n\n"
        help_message += "/help              - Help \n"
        help_message += "/connect {host}    - Connect to a known IP \n"
        help_message += "/search            - Search the network for hosts \n"
        help_message += "/clear             - Clear the current panel (doesn't delete log) \n"
        help_message += "\n"
        help_message += "/about             - About CoPa \n"
        help_message += "/exit              - Exit CoPa \n"

        return help_message

    def execute(self):
        pass


class Connect(Command):

    def __init__(self, params):
        super(Connect, self).__init__()

        if len(params) is not 1:
            raise CommandException("A valid host must be provided.")

        self.host = params[0]

    def get_message(self):
        return "Connecting to " + self.host

    def execute(self):
        pass


class Clear(Command):

    def get_message(self):
        return ""

    def execute(self):
        pass


class Exit(Command):

    def get_message(self):
        return ""

    def execute(self):
        sys.exit(0)
