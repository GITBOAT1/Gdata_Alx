#!/usr/bin/python3
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
""" simple function to help make tikinter easy for diplay """


def center_window(root, width=300, height=200):
    """ This module help the difens the position of
        the window
    """
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


def about():
    """ This is a popup message regarding the creator """
    mb.showinfo('About!', 'This is a Simple program(garage info 0.2)'
                'to keep record of a garage. For more info Email the'
                'creator Boateng,on email:boat232001@yahoo.com ')


def bt(win, name, title, row, column):
    """ function for creating buttons no command
    first button
    """
    name = Button(win, text=title, width=buttomw)
    name.grid(row=row, column=column)


def bt1(win, name, title, row, column, command="None"):
    """ This is the buncton for creating buttons """
    name = Button(win, text=title, width=10, command=command)
    name.grid(row=row, column=column)


def childWindow(child, main, title):
    """ This is for preventing main window when the
    child window is opened
    """
    child.title(title)
    child.transient(main)
    child.grab_set()
    main.wait_window(child)


def check_box():
    """ check box """
    name.grid(row=row, column=column)


def entries(name, row, column, txtvar):
    """ Entries """
    name = Entry(defaultwin, textvariable=textvar)
    name.grid(row=row, column=column)


def leb(win, words, ro, col):
    """ lables function """
    name = Label(win, text=words)
    name.grid(row=ro, column=col, sticky=W, pady=4, padx=4)


def scrollbar(name, config, row, column, rspan):
    """ scrollbar function
        config for the list where list needs to be scrolled
    """
    name = Scrollbar(window)
    name.grid(row=row, column=column, rowspan=rspan)
    config.configure(yscrollcommand=name.set)
    name.configure(command=config.yview)
