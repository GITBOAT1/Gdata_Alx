#!/usr/bin/python3
from modles.win_help import center_window, about, bt1
import modles.view1
import tkinter as tk
#from tkinter import *
""" The user interface """


window = tk.Tk()
center_window(window, 600, 299)
window.title("Garage Data")
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label = "New")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=window.quit)
menubar.add_cascade(label="Menu",menu =filemenu)
helpmenu = tk.Menu(menubar,tearoff=0)
helpmenu.add_command(label = "About",command = about)
menubar.add_cascade(label="Help",menu =helpmenu)
window.config(menu=menubar)
buttomw = 12
defaultwin = "windows"
txtvar = tk.StringVar()

""" containers """
container = tk.Frame()
container.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
container1 = tk.Frame()
container1.grid(row=1, column=5, padx=5, pady=5)

""" buttons for the display """
bt1(container1, name="b8",title="Costed  Jobs",row=0, column=10,command = lambda e='CLOSED': view1(e))
#bt1(container1, name="b2",title="View jobs", row=1, column=10, command=view1(e))
bt1(container1, name="b3",title="Available Jobs",row=3, column=10,command = lambda e='WAITING': view1(e))
bt1(container1, name="b4",title="Completed Jobs",row=4, column=10,command = lambda e='COMPLETED': view1(e))
#bt1(container1, name="b5",title="Add Jobs",row=5, column=10,command=job_card)
#bt1(container1, name="b6",title="Add New Tech",row=6, column=10, command=Tech)
#bt1(container1, name="b7",title="Exit",row=7, column=10, command=window.quit)





""" main() """
window.mainloop()
