class CommandException(Exception):

    def __init__(self, message=''):
        super(CommandException, self).__init__(self, message=message)


class GuiException(Exception):

    def __init__(self, message=''):
        super(GuiException, self).__init__(self, message=message)

