#!/usr/bin/python3
from tkinter import messagebox as mb
import tkinter as tk
import database.db
""" This model is a child window for
    which open's anew window, for technician
    data entry
"""


def Tech():
    """ Tech child window """
    tc = tk.Toplevel()
    # tc.iconbitmap(r'C:\Users\obi j\Downloads\cs50 files\pset9\web\pset8\python gui\gui.ico')
    center_window(tc, 400, 200)

    def quit(event):
        """ exit """
        tc.destroy()

    te = tech(tc, Tfields)

    def ft():
        """ """
        e = techfetch(te)
        if (e[0] == "" or e[1] == "" or e[2] == "" or e[3] == ""):
            mb.showinfo('Fields Empty', 'Fields cant be empty')
        else:
            tec = (e[0], e[1], e[2], e[3])
            ch1 = db.execute("SELECT name FROM customer WHERE name =?", (tec[0],))
            check = ch1.fetchall()

            # check if name exit
            if check:
                print("")
                mb.showinfo('user exit', 'tech already exit')
            else:
                db.execute("INSERT INTO tech(name, contact, title, year)VALUES (?, ?, ?, ?)", tuple(tec))
                conn.commit()
                mb.showinfo('Tech', 'Tech Added')
                tc.destroy()

    # The buttom side
    row = tk.Frame(tc)
    note = Button(row, text="Add", width=buttomw, command=ft)

    # note.bind('<Button-0>',vii)
    note2 = Button(row, text="Close", width=buttomw)

    row.pack(side=tk.TOP, fill=tk.X, padx=5)
    note.pack(side=tk.LEFT, expand=tk.YES)

    note2.bind('<Button-1>', quit)
    note2.pack(side=tk.LEFT, expand=tk.YES)
