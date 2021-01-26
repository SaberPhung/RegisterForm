from tkinter import * #import everything from tkinter
import sqlite3

box = Tk()
box.geometry("500x300")

#defind submit function

def database():
    Name=namevalue.get()
    Mobile=mobilevalue.get()
    Email=emailvalue.get()
    Gender=gendervalue.get()
    Title=titlevalue.get()
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student (Name TEXT,Mobile TEXT,Email TEXT,Gender TEXT,title TEXT)')
    cursor.execute('INSERT INTO Student (Name,Mobile,Email,Gender,Title) VALUES(?,?,?,?,?)',(Name,Mobile,Email,Gender,Title,))
    conn.commit()


# Heading
Label(box, text="Registation Form", font="ar 15 bold").grid(row=0, column=3)

#Field name

name   = Label(box, text="Name")
mobile = Label(box, text="Mobile")
gender = Label(box, text="Gender")
email  = Label(box, text="Email")
title  = Label(box, text="Title")

# Packing fields
name  .grid  (row=1, column=2)
mobile.grid  (row=2, column=2)
gender.grid  (row=3, column=2)
email .grid  (row=4, column=2)
title .grid  (row=5, column=2)

# Variable for storing data
namevalue = StringVar()
mobilevalue = StringVar()
gendervalue = StringVar()
emailvalue = StringVar()
titlevalue = StringVar()
checkvalue = IntVar()

# Creating Entry fields
nameentry = Entry(box, textvariable =namevalue)
mobileentry = Entry(box, textvariable =mobilevalue)
genderentry = Entry(box, textvariable =gendervalue)
emailentry = Entry(box, textvariable =emailvalue)
titleentry = Entry(box, textvariable =titlevalue)

# Packing entry fields
nameentry.grid(row=1, column=3)
mobileentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emailentry.grid(row=4, column=3)
titleentry.grid(row=5, column=3)

# Creating Checkbox
checkbutton= Checkbutton(text="Done", variable =checkvalue)
checkbutton.grid(row=6, column=3)

# Creating submit button
Button(text="Submit", command=database).grid(row=7, column=3)



box.mainloop()
