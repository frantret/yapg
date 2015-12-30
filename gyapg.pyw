#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""\
gyapg: GUI for yapg (yet another password generator)
"""


import yapg
import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    """\
    Builds a basic window.
    """

    def __init__(self, title):
        super().__init__()
        self.title(title)
        # assigns closing the window to the escape key
        self.bind("<Escape>", lambda e: self.destroy())

    def give_space(self):
        """\
        Gives some padding around all the elements.
        """
        for Child in self.winfo_children():
            Child.grid_configure(padx=5, pady=5)


class About(Window):
    """\
    Builds an "about" window.
    """

    def __init__(self):
        super().__init__("About gyapg")
        self.columnconfigure(0, weight=1)
        # sets the grid
        TxtDoc = ttk.Label(self, text=__doc__.strip())
        TxtDoc.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.give_space()
        # assigns closing the window to the return key and click
        self.bind("<Return>", lambda e: self.destroy())
        self.bind("<Button-1>", lambda e: self.destroy())


class PasswordGenerator(Window):
    """\
    Builds the main password generator window.
    """

    def __init__(self):
        super().__init__("gyapg")
        self.columnconfigure(1, weight=1)
        # initializes the variables
        self.DicSettings = dict(yapg.DEFAULT)
        self.TempSettings = dict(yapg.DEFAULT)
        self.TkSettings = {}
        self.TkSettings["length"] = tk.StringVar()
        self.TkSettings["digits"] = tk.BooleanVar()
        self.TkSettings["lowercase"] = tk.BooleanVar()
        self.TkSettings["uppercase"] = tk.BooleanVar()
        self.TkSettings["punctuation"] = tk.BooleanVar()
        self.TkSettings["homoglyphs"] = tk.BooleanVar()
        for Key in self.TkSettings.keys():
            self.TkSettings[Key].set(self.DicSettings[Key])
        self.VarList = tk.StringVar()
        self.VarPassword = tk.StringVar()
        # sets the grid elements
        TxtLength = ttk.Label(self, text="length:")
        LengthEnt = ttk.Entry(
            self,
            textvariable=self.TkSettings["length"],
            foreground='black',
            background='white'
        )
        TxtChars = ttk.Label(self, text="characters")
        ButDigits = ttk.Checkbutton(
            self,
            text=yapg.HELP["digits"],
            variable=self.TkSettings["digits"]
        )
        ButLowercase = ttk.Checkbutton(
            self,
            text=yapg.HELP["lowercase"],
            variable=self.TkSettings["lowercase"]
        )
        ButUppercase = ttk.Checkbutton(
            self,
            text=yapg.HELP["uppercase"],
            variable=self.TkSettings["uppercase"]
        )
        ButPunctuation = ttk.Checkbutton(
            self,
            text=yapg.HELP["punctuation"],
            variable=self.TkSettings["punctuation"]
        )
        ButHomoglyphs = ttk.Checkbutton(
            self,
            text=yapg.HELP["homoglyphs"],
            variable=self.TkSettings["homoglyphs"]
        )
        ButAbout = ttk.Button(
            self,
            text="about",
            command=self.build_about
        )
        ButGenerate = ttk.Button(
            self,
            text="generate",
            command=self.generate
        )
        TxtPassword = ttk.Label(self, textvariable=self.VarPassword)
        ButCopy = ttk.Button(
            self,
            text="copy to clipboard",
            command=self.copy
        )
        # sets the grid layout
        TxtLength.grid(row=0, column=0, sticky=tk.W)
        LengthEnt.grid(row=0, column=1, sticky=(tk.W, tk.E))
        TxtChars.grid(row=0, column=2, sticky=tk.W)
        ButDigits.grid(row=1, column=1, sticky=(tk.W, tk.E))
        ButLowercase.grid(row=2, column=1, sticky=(tk.W, tk.E))
        ButUppercase.grid(row=3, column=1, sticky=(tk.W, tk.E))
        ButPunctuation.grid(row=4, column=1, sticky=(tk.W, tk.E))
        ButHomoglyphs.grid(row=5, column=1, sticky=(tk.W, tk.E))
        ButAbout.grid(row=5, column=2, sticky=tk.E)
        ButGenerate.grid(row=6, column=0, sticky=tk.W)
        TxtPassword.grid(row=6, column=1, sticky=(tk.W, tk.E))
        ButCopy.grid(row=6, column=2, sticky=tk.E)
        self.give_space()
        # gives focus to the entry field
        LengthEnt.focus()
        # assigns the calculate function to the return key
        # (in addition to the button)
        self.bind("<F1>", self.build_about)
        self.bind("<Return>", self.generate)
        self.bind("<Control-c>", self.copy)

    def build_about(self, *args):
        """\
        Builds an "about" window.
        """
        self.AboutWin = About()
        self.AboutWin.mainloop()

    def generate(self, *args):
        """\
        Generates a password and assigns it.
        """
        # transfers GUI settings to the operational dictionary
        self.DicSettings = dict()
        for Key in self.TkSettings.keys():
            self.DicSettings[Key] = self.TkSettings[Key].get()
        # if there is any change in the settings, re-builds the list
        if self.TempSettings != self.DicSettings:
            self.TempSettings = self.DicSettings
            self.VarList.set(yapg.build_list(**self.DicSettings))
        # builds a new password
        self.VarPassword.set(
            yapg.build_pwd(self.VarList.get(), **self.DicSettings)
        )

    def copy(self, *args):
        """\
        Copies the password to the clipboard.
        """
        Password = self.VarPassword.get()
        if Password and not Password.lower().startswith("error"):
            self.clipboard_clear()
            self.clipboard_append(Password)


if __name__ == "__main__":
    Root = PasswordGenerator()
    Root.mainloop()
