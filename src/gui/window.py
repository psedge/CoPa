import tkinter as tk

from util.exceptions import GuiException


class Window:
    _window = None
    _entry = None
    _button = None
    _messages = None
    _q = None

    def __init__(self, queue):
        # Open tk window
        self._window = tk.Tk()
        self._window.geometry("600x400+600+400"),
        self._window.title('CoPa - Secure Local Messaging')
        self._window.configure(background='black')

        # Init text area
        self._messages = tk.Frame(self._window, background='white')
        self._messages.pack(expand=True, fill=tk.X, side=tk.TOP, anchor='n')

        # Init text entry form and grid
        self._entry = tk.Entry(self._window, bd=5, relief=tk.FLAT, exportselection=0)
        self._entry.focus()
        self._entry.bind('<Return>', self._button_click)
        self._entry.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        # Welcome banner
        self.put("CoPa v0.1 - 0 clients connected. \n", tk.RAISED)

        # Init 'Send' button
        self._button = tk.Button(self._window, text="Send", command=self._button_click)
        self._button.pack(side=tk.LEFT)

        # Register the queue
        self._q = queue
        return

    def __call__(self, *args, **kwargs):
        # Start gooey
        self._window.mainloop()

    def _button_click(self, event=None):
        """
        Take input from message box, pass to callback.

        :return:
        """
        input = self._entry.get()
        self.put(input)
        self._entry.delete(0, tk.END)
        self._q.put(input)


    def put(self, message, style=tk.SUNKEN):
        """
        Add a message to the GUI.

        :param message:
        :param style:
        :return:
        """
        var = tk.StringVar()

        label = tk.Message(self._messages, textvariable=var, relief=style, anchor='w', bg='white', width=600, padx=5, pady=5)
        var.set(message)

        label.pack(fill=tk.X, expand=True, side=tk.TOP)

    def clear(self):
        for widget in self._messages.winfo_children()[1:]:
            widget.destroy()

