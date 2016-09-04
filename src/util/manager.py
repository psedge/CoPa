from messaging.fomats import Message
from util.selector import Selector


class Manager:

    def __init__(self, gui):
        self.gui = gui

    def process_input(self, input):
        """
        Process input from GUI. Will be either command or message.

        :param input:
        :return:
        """
        if self.is_command(input):
            command_dict = self.split_input_to_command(input)
            command = Selector(
                string=command_dict['command'],
                params=command_dict['args'],
            )
            command.command.gui = self.gui
            command.execute()

            return self.put_to_gui(command.get_output())

        message = Message(input)
        return self.put_to_gui("(You): " + str(message))

    def put_to_gui(self, string):
        self.gui.put(string)

    @staticmethod
    def is_command(input):
        first_character = input[0]
        if first_character == '/':
            return True
        return False

    @staticmethod
    def split_input_to_command(input):
        parts = input.lstrip("/").split(" ")
        return {'command': parts.pop(0), 'args': parts}



