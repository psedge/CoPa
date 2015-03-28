import sys
import tkinter as tk
import os
import time


class Gui:
    _dbg = None
    _window = None
    _entry = None
    _button = None
    _callback = None
    _action_callback = None
    _messages = None

    def __init__(self, log, callback, _action_callback):
        self._dbg = log
        self._dbg.write('Starting Tk window', log.DEBUG)

        # Register callback for on send / receive message
        if callable(callback) and callable(_action_callback):
            self._callback = callback
            self._action_callback = _action_callback
        else:
            raise Exception('Callback isn\'t callable.')

        # Open tk window
        self._window = tk.Tk()
        self._window.geometry("600x400+600+400"),
        self._window.title('CoPa - Local Messaging')
        self._window.configure(background='black')

        # Init text area
        self._messages = tk.Frame(self._window, background='white')
        self._messages.pack(expand=True, fill=tk.X, side=tk.TOP, anchor='n')

        # Init text entry form and grid
        self._entry = tk.Entry(self._window, bd=5, relief=tk.FLAT, exportselection=0)
        self._entry.focus()
        self._entry.bind('<Return>', self.button_click)
        self._entry.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        # Welcome banner
        self.insert_message("Welcome to CoPa v0.1 - 0 clients connected. \n")

        # Init 'Send' button
        self._button = tk.Button(self._window, text="Send", command=self.button_click)
        self._button.pack(side=tk.LEFT)

        # Start gooey
        self._window.mainloop()
        return

    def button_click(self, event=None):
        self.process_message(self._entry.get())

    def process_message(self, message):
        first_word = message.split(' ')[0]
        self._entry.delete(0, tk.END)

        if message == '?':
            help_message = "CoPa - The (Co)py(Pa)ste Messaging Application. \nv0.1\n\n"
            help_message += "?              - Help \n"
            help_message += "connect {host} - Connect to a known IP \n"
            help_message += "recon          - Search the network for hosts \n"
            help_message += "clear          - Clear the current panel (doesn't delete log) \n"
            help_message += "\n";
            help_message += "about          - About CoPa \n"
            help_message += "exit           - Exit CoPa \n"

            self.insert_message(help_message)
        elif first_word == 'connect':
            addr = message.split(' ')[1]
            self._action_callback('connect', {"addr": addr})
        else:
            self.send(message)

    def insert_message(self, message, addr = None):

        var = tk.StringVar()
        if addr:
            label = tk.Message(self._messages, textvariable=var, relief=tk.FLAT, anchor='w', bg='#f0f0f0', width=600, padx=5, pady=5)
            var.set(addr + ' ' + message)
        else:
            label = tk.Message(self._messages, textvariable=var, relief=tk.FLAT, anchor='w', bg='white', width=600, padx=5, pady=5)
            var.set(message)

        label.pack(fill=tk.X, expand=True, side=tk.TOP)

    def send(self, message):
        self.insert_message(message)

        self._dbg.write(message, self._dbg.DEBUG)

        self._callback({"message": message, "method": "OUT", "args": {"time": time.time()}})

    def receive(self, message, addr):
        self.insert_message(self, message, addr)
