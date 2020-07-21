from tkinter import * 

from tkinter import messagebox

import mysql.connector
import sys

def CheckLogin():
    global username
    username = E1.get()
    global server
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

    userlogin.destroy()
    
    global root
    root = Tk()
    #root.geometry("1280x720")

    title = (username + "@" + server)
    w = Label(root, text=title)
    w.pack(side=TOP)

    B1 = Button(root, text='Nachrichten lesen', width=25, bg="blue", command=ReadMessages)
    B1.pack(side=LEFT)

    B2 = Button(root, text="Nachricht schreiben", width=25, bg="white", command=WriteMessage)
    B2.pack(side=LEFT)

    B3 = Button(root, text='Exit', width=25, command=root.destroy)
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
    mycursor = mydb.cursor()

    sqlFormula = "INSERT INTO chatroom1 (username, text) VALUES (%s, %s)"
    nachrichtpacket = (username, Message)

    mycursor.execute(sqlFormula, nachrichtpacket)

    mydb.commit()

    print("Nachricht gesendet: " + Message)
    WriteWindow.destroy()

def ReadMessages():
    print("Loading Messages..")

    MessageWindow = Tk()

    global mydb
    mydb = mysql.connector.connect(
        host=server,
        user="chatuser",
        passwd="chatpasswort",
        database="chat_datenbank"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM chatroom1")

    myresult = mycursor.fetchall()
        
    if myresult == []:
        print("Keine Nachrichten uwu")
        L = Label(MessageWindow, text = "Keine Nachrichten uwu")
        L.pack()
    else:    
        for row in myresult:
            Message = row[1] + ": " + row[2]
            print(Message)
            L = Label(MessageWindow, text = Message)
            L.pack()


userlogin = Tk()

L1 = Label(userlogin, text = "Username:")
L1.pack(side = LEFT)

E1 = Entry(userlogin, bd = 1)
E1.pack(side = LEFT)

L2 = Label(userlogin, text = "MySQL Server:")
L2.pack(side = LEFT)

E2 = Entry(userlogin, bd = 1)
E2.pack(side = LEFT)

B1 = Button(userlogin, text='Login', width=10, bg="white", command = CheckLogin)
B1.pack(side = RIGHT)

userlogin.mainloop()
