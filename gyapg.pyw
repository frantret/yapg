#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gyapg: graphical user interface for yapg (yet another password \
generator)
"""

import tkinter as tk
from tkinter import ttk

import yapg


class Window(tk.Tk):
    """Builds a basic window."""

    def __init__(self, title):
        super().__init__()
        self.title(title)
        # Assigns closing the window to the escape key.
        self.bind("<Escape>", lambda e: self.destroy())

    def give_space(self):
        """Gives some padding around all the elements."""
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)


class About(Window):
    """Builds an "about" window."""

    def __init__(self):
        super().__init__("About gyapg")
        self.columnconfigure(0, weight=1)
        # Sets the grid.
        txt_doc = ttk.Label(self, text=f"{__doc__.strip()}\nversion {yapg.__version__}")
        txt_doc.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.give_space()
        # Assigns closing the window to the return key and click.
        self.bind("<Return>", lambda e: self.destroy())
        self.bind("<Button-1>", lambda e: self.destroy())


class PasswordGenerator(Window):
    """Builds the main password generator window."""

    def __init__(self):
        super().__init__("gyapg")
        self.columnconfigure(1, weight=1)
        # Initializes the variables.
        self.cfg_dic = dict(yapg.DEFAULT)
        self.cfg_tmp = dict(yapg.DEFAULT)
        self.cfg_tk = dict()
        self.cfg_tk["length"] = tk.StringVar()
        self.cfg_tk["digits"] = tk.BooleanVar()
        self.cfg_tk["lowercase"] = tk.BooleanVar()
        self.cfg_tk["uppercase"] = tk.BooleanVar()
        self.cfg_tk["punctuation"] = tk.BooleanVar()
        self.cfg_tk["homoglyphs"] = tk.BooleanVar()
        self.cfg_tk["compatible"] = tk.BooleanVar()
        for config_item in self.cfg_tk:
            self.cfg_tk[config_item].set(self.cfg_dic[config_item])
        self.var_list = tk.StringVar()
        self.var_pwd = tk.StringVar()
        # Sets the grid elements.
        txt_length = ttk.Label(self, text="length:")
        ent_length = ttk.Entry(
            self,
            textvariable=self.cfg_tk["length"],
            foreground="black",
            background="white",
        )
        txt_chars = ttk.Label(self, text=yapg.HELP_CHARS)
        chk_digits = ttk.Checkbutton(
            self, text=yapg.HELP["digits"], variable=self.cfg_tk["digits"]
        )
        chk_lowercase = ttk.Checkbutton(
            self, text=yapg.HELP["lowercase"], variable=self.cfg_tk["lowercase"]
        )
        chk_uppercase = ttk.Checkbutton(
            self, text=yapg.HELP["uppercase"], variable=self.cfg_tk["uppercase"]
        )
        chk_punctuation = ttk.Checkbutton(
            self, text=yapg.HELP["punctuation"], variable=self.cfg_tk["punctuation"]
        )
        chk_homoglyphs = ttk.Checkbutton(
            self, text=yapg.HELP["homoglyphs"], variable=self.cfg_tk["homoglyphs"]
        )
        chk_compatible = ttk.Checkbutton(
            self, text=yapg.HELP["compatible"], variable=self.cfg_tk["compatible"]
        )
        but_about = ttk.Button(self, text="about", command=self.build_about)
        but_generate = ttk.Button(self, text="generate", command=self.generate)
        txt_password = ttk.Label(self, textvariable=self.var_pwd, font="TkFixedFont")
        but_copy = ttk.Button(self, text="copy to clipboard", command=self.copy)
        # Sets the grid layout.
        txt_length.grid(row=0, column=0, sticky=tk.W)
        ent_length.grid(row=0, column=1, sticky=(tk.W, tk.E))
        txt_chars.grid(row=0, column=2, sticky=tk.W)
        chk_digits.grid(row=1, column=1, sticky=(tk.W, tk.E))
        chk_lowercase.grid(row=2, column=1, sticky=(tk.W, tk.E))
        chk_uppercase.grid(row=3, column=1, sticky=(tk.W, tk.E))
        chk_punctuation.grid(row=4, column=1, sticky=(tk.W, tk.E))
        chk_homoglyphs.grid(row=5, column=1, sticky=(tk.W, tk.E))
        chk_compatible.grid(row=6, column=1, sticky=(tk.W, tk.E))
        but_about.grid(row=6, column=2, sticky=tk.E)
        but_generate.grid(row=7, column=0, sticky=tk.W)
        txt_password.grid(row=7, column=1, sticky=(tk.W, tk.E))
        but_copy.grid(row=7, column=2, sticky=tk.E)
        self.give_space()
        # Gives focus to the entry field.
        ent_length.focus()
        # Assigns the functions to keys (in addition to the buttons).
        self.bind("<F1>", self.build_about)
        self.bind("<Return>", self.generate)
        self.bind("<Control-c>", self.copy)
        # Builds the list of allowed characters.
        self.var_list.set(yapg.build_list(**self.cfg_dic))

    # In the following methods, Pylint complains "W0613: Unused argument 'args'",
    # but it is required by Tkinter.

    def build_about(self, *args):
        """Builds an "about" window."""
        # Pylint complains "W0201: Attribute 'win_about' defined outside __init__",
        # but moving the following line to init breaks the child window behavior.
        self.win_about = About()
        self.win_about.mainloop()

    def generate(self, *args):
        """Generates a password and assigns it."""
        # Transfers GUI settings to the operational dictionary.
        self.cfg_dic = dict()
        for config_item in self.cfg_tk:
            self.cfg_dic[config_item] = self.cfg_tk[config_item].get()
        # If there is any change in the settings, re-builds the list.
        if self.cfg_tmp != self.cfg_dic:
            self.cfg_tmp = self.cfg_dic
            self.var_list.set(yapg.build_list(**self.cfg_dic))
        # Builds a new password.
        self.var_pwd.set(yapg.build_pwd(self.var_list.get(), **self.cfg_dic))

    def copy(self, *args):
        """Copies the password to the clipboard."""
        pwd = self.var_pwd.get()
        if pwd and not pwd.lower().startswith("error"):
            self.clipboard_clear()
            self.clipboard_append(pwd)


if __name__ == "__main__":
    ROOT = PasswordGenerator()
    ROOT.mainloop()
