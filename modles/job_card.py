#!/usr/bin/python3
"""This where we creat the job card """

from tkinter import messagebox as mb
import tkinter as tk
import database.db
from datetime import *

def job_card():
    """ model to create a date for the car """
    fields = 'Full Name', 'Contact:', 'Vin', 'Reg Number'
    jc = Toplevel()
    # jc.iconbitmap(r'\gui\gui.ico')
    a = []
    #jc.geometry('450x200')
    center_window(jc,750,500)
    #configure window
    job = makeform(jc, fields)
    year = datetime.today().year
    YEARS = [year - i for i in range(100)]

    
    def fetch(entries):
        """ first entries """
        text=[]
        for entry in entries:
            field = entry[0]
            text.append(entry[1].get())
            #print('%s: "%s"' % (field, text))
        return text

    def makeform(root, fields):
        """ make a form """
        entries = []
        for field in fields:
            row = tk.Frame(root)
            lab = tk.Label(row, width=15, text=field, anchor='w')
            ent = tk.Entry(row,bg="light blue")
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append((field, ent))
        return entries

    #screen position
    def center_window(root,width=300, height=200):
        # get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        
    #radio buttom for notes
    def ShowChoice(v):
        print(v.get())
        
    def job_type(root,v):
        jobte = [
        ("AC",1),
        ("ELECTRICAL",2),
        ("MECHANICAL",3),
        ("BODY",4),
        ]
        #ShowChoice(v)
        tk.Label(root,text="""Select Type:""", justify = tk.LEFT,padx = 20).pack()

        for val, jobte in enumerate(jobte):
            tk.Radiobutton(root,
                           text=jobte,
                           padx = 20,
                           variable=v,
                           command=lambda e=v: ShowChoice(e),
                           value=val).pack(side=tk.LEFT)

    #add # NOTE:
    def addnote(root):
        """ """
        row = tk.Frame(root)
        lab = tk.Text(row,height=2,width=20,bg="light blue")
        #ent = tk.Entry(row,bg="light blue")
        #row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        row.pack(side=tk.BOTTOM, fill=tk.X,padx=5)
        lab.pack(side=tk.LEFT,expand=tk.YES, fill=tk.X)"""
        #ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X) """

    # Concern
    def add_concern(root):
        """ """
        txt = []
        S = tk.Scrollbar(root)
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text= "concern",anchor='w')
        ent = tk.Text(row,height=10,width=20,bg="light blue")
        # ent = tk.Entry(row,bg="light blue")
        # row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        row.pack(side=tk.TOP, fill=tk.X,padx=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        ent.config(yscrollcommand=S.set)
        a = ent.get("1.0",'end-1c')
        return a


    # get values from fields
    def fetchme():
        """ Get maker and modle name """
        z=fetch(job)
        z.append(year.get())
        z.append(carvar.get())
        z.append(note.get("1.0","end-1c"))
        z.append(ent.get("1.0","end-1c"))
        DF = "WAITING"

        jobte = ["AC","ELECTRICAL","MECHANICAL","BODY"]
        a = v.get()
        for i in range(3):
            if(a ==i ):
                z.append(jobte[i])
        if(z[0]== "" or z[1]== "" or z[2]== "" or z[3]== ""or  z[7]== "" ):
            mb.showinfo('Fields Empty', 'Fields cannot be empty')

        else:
            check = db.execute("SELECT name FROM customer WHERE name=?", (z[0],))
            check1=check.fetchall()
            if(check1):
                # grab the last insert  auto increament
                c_id1 = db.execute("SELECT id FROM customer WHERE name =?", (z[0],))
                c_id = c_id1.fetchall()
                c_id = c_id[0].get("id")
                h =int(c_id)
                DF = "WAITING"
                cost ="N/A"
                std1 =(z[2],z[3],z[4],z[5],h,DF,cost)
                db.execute("INSERT INTO vehicls(vin, reg, year, maker, job_id, status,cost) VALUES (?,?,?,?,?,?,?)", tuple(std1))

                std3 =(c_id,z[6],z[7],z[8],h)
                db.execute("INSERT INTO cust_concern (job,note,type,cust_id) VALUES (?,?,?,?)", tuple(std3))
                conn.commit()
                mb.showinfo('Note', 'Data Added')
                #jc.destroy()

            else:
                # add to the no of cars the Tech  has
                # create new customer and insert data int customer TABLE
                stu = (z[0],z[1])
                db.execute("INSERT INTO customer(name,contact) VALUES (?,?)", tuple(stu))
                conn.commit()

                #grab the last insert  auto increament
                c_id2 = db.execute("SELECT LAST_INSERT_ROWID()")
                c_id1 = c_id2.fetchall()
                h = int(c_id1[0][0])
                cost ="N/A"
                stu11 =(z[2], z[3], z[4], z[5], h, DF, cost)
                db.execute("INSERT INTO vehicles(vin, reg, year, maker, job_id, status,
                cost) VALUES (?, ?, ?,?,?,?,?)", tuple(stu11) )
                conn.commit()

                # grab the last insert  auto increament
                c_id1 = db.execute("SELECT LAST_INSERT_ROWID()")
                c_id1 = c_id2.fetchall()

                # c_id1= c_id1[0].get("LAST_INSERT_ROWID()")
                h = int(c_id1[0][0])

                stu3 =(z[7],z[6],z[8],h)
                db.execute("INSERT INTO cust_concern (job, note, type, car_id) VALUES (?,?,?,?)", tuple(stu3))
                mb.showinfo('Note', 'Customer Added')
                conn.commit()
                view1()
                jc.destroy()
