class CommandException(Exception):

    def __init__(self, message=''):
        super(CommandException, self).__init__(self, message=message)


class GuiException(Exception):

    def __init__(self, message=''):
        super(GuiException, self).__init__(self, message=message)


class TransportMethodException(Exception):

    def __init__(self, message=''):
        super(TransportMethodException, self).__init__(self, message=message)


class TransportException(Exception):

    def __init__(self, message=''):
        super(TransportException, self).__init__(self, message=message)

