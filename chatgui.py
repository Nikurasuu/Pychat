from tkinter import * 

from tkinter import messagebox

def MainWindow():
    username = E1.get()
    userlogin.destroy()

    root = Tk()
    root.geometry("1280x720")

    title = ("Willkommen bei Pychat " + username + "!")
    w = Label(root, text=title)
    w.pack()

    B1 = Button(root, text='Nachrichten aktualisieren', width=25)
    B1.pack()

    B2 = Button(root, text='Stop', width=25, command=root.destroy)
    B2.pack()

    root.mainloop()

userlogin = Tk()

L1 = Label(userlogin, text = "User Name")
L1.pack( side = LEFT)

B1 = Button(userlogin, text='Login', width=10, command = MainWindow)
B1.pack(side = RIGHT)

E1 = Entry(userlogin, bd = 5)
E1.pack(side = RIGHT)

userlogin.mainloop()
