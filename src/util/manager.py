from messaging.formatting import Message
from messaging.transport import IMCP
from util.selector import Selector
from multiprocessing import Queue, Process


class Manager:

    def __init__(self):
        self.queue = Queue()
        self.queue.cancel_join_thread()

    def process_input(self, input):
        """
        Process input from GUI. Will be either command or message.

        :param input:
        :return:
        """

        print("Starting child process with input: '" + input + "'")

        t1 = Process(target=self.work, args=(input,))
        t1.start()
        t1.join()

    def work(self, input):
        if Command.is_command(input):
            command_dict = Command.split_input_to_command(input)
            command = Selector(
                string=command_dict['command'],
                params=command_dict['args'],
            )
            command.execute()

            return self.queue.put("> " + command.get_output())

        message = Message(input)
        if message.send(IMCP):
            return self.queue.put("(You): " + str(message))

        return self.queue.put("(failed): " + str(message))


class Command:

    @staticmethod
    def is_command(input):
        """
        Determines if the input is intended as a command.

        :param input:
        :return:
        """
        first_character = input[0]
        if first_character == '/':
            return True
        return False

    @staticmethod
    def split_input_to_command(input):
        """
        Converts a command string to a dict.

        :param input:
        :return:
        """
        parts = input.lstrip("/").split(" ")
        return {'command': parts.pop(0), 'args': parts}



