from tkinter import * 

from tkinter import messagebox

import mysql.connector
import sys

def CheckLogin():
    server = E2.get()
    print("Connecting to " + server)
    try:
        global mydb
        mydb = mysql.connector.connect(
            host=server,
            user="chatuser",
            passwd="chatpasswort",
            database="chat_datenbank"
        )
        OpenMainWindow()
    except:
        print("Failed Login or opening MainWindow()")


def OpenMainWindow():

    print(mydb)

    username = E1.get()
    server = E2.get()
    userlogin.destroy()
    
    root = Tk()
    root.geometry("1280x720")

    title = (username + "@" + server)
    w = Label(root, text=title)
    w.pack(side=LEFT)

    B1 = Button(root, text='Nachrichten aktualisieren', width=25, command=ReadMessages)
    B1.pack(side=LEFT)

    B2 = Button(root, text="Nachricht schreiben", width=25, command=WriteMessage)
    B2.pack(side=LEFT)

    B3 = Button(root, text='Stop', width=25, command=root.destroy)
    B3.pack(side=LEFT)

    root.mainloop()


def WriteMessage():
        
    global WriteWindow
    WriteWindow = Tk()

    global MessageEntry
    MessageEntry = Entry(WriteWindow, bd = 1)
    MessageEntry.pack(side = LEFT)

    B1 = Button(WriteWindow, text='Send', width=10, command = SendMessage)
    B1.pack(side = RIGHT)

    WriteWindow.mainloop()

def SendMessage():
    Message = MessageEntry.get()
    print(Message)
    WriteWindow.destroy()

def ReadMessages():
    print("Loading Messages..")


userlogin = Tk()

L1 = Label(userlogin, text = "Username:")
L1.pack(side = LEFT)

E1 = Entry(userlogin, bd = 1)
E1.pack(side = LEFT)

L2 = Label(userlogin, text = "MySQL Server:")
L2.pack(side = LEFT)

E2 = Entry(userlogin, bd = 1)
E2.pack(side = LEFT)

B1 = Button(userlogin, text='Login', width=10, command = CheckLogin)
B1.pack(side = RIGHT)

userlogin.mainloop()
