import tkinter as tk
from settings import *


class Window:

    def __init__(self, manager):
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
        self._entry.bind('<Return>', self._handle)
        self._entry.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        # Welcome banner
        self._put("CoPa v" + VERSION + " - 0 clients connected. \n", tk.RAISED)

        # Init 'Send' button
        self._button = tk.Button(self._window, text="Send", command=self._handle)
        self._button.pack(side=tk.LEFT)

        # Register the manager
        self._m = manager
        self._window.after(100, self._get_messages, self._m.queue)

    def _get_messages(self, q):
        """
        Get messages from the child processes and add them to the messages area.

        :param q:
        :return:
        """
        while q.qsize() is not 0:
            self._put(q.get())

        self._window.after(100, self._get_messages, self._m.queue)

    def _handle(self, event=None):
        """
        Take input from message box, pass to callback.

        :return:
        """
        self._m.process_input(self._entry.get())
        self._entry.delete(0, tk.END)

    def _put(self, message, style=tk.SUNKEN):
        """
        Add a message to the GUI.

        :param message:
        :param style:
        :return:
        """

        if message is None or message is "":
            pass

        var = tk.StringVar()

        label = tk.Message(self._messages, textvariable=var, relief=style, anchor='w', bg='white', width=600, padx=5, pady=5)
        var.set(message)

        label.pack(fill=tk.X, expand=True, side=tk.TOP)

        self._messages.update()
        self._window.update()

    def open(self, *args, **kwargs):
        self._window.mainloop()

    def close(self):
        self._window.destroy()

    def clear(self):
        for widget in self._messages.winfo_children()[1:]:
            widget.destroy()

