import mysql.connector
import time

def nachrichten_auslesen():
    #Nachrichten auslesen und anzeigen
        print("Aktuelle Nachrichten: ")
        print("")

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM chatroom1")

        myresult = mycursor.fetchall()
        
        print(myresult)

        for row in myresult:
            print("(" + str(row[0]) + ") " + row[1] + ": " + row[2])
            time.sleep(0.05)

        print("")

def passwort_überprüfen():
    passwort = input("Passwort eingeben: ")
    
    mycursor = mydb.cursor()
    sqlFormula = "SELECT password FROM users WHERE username = '%s'"
    packet = (username)

    mycursor.execute(sqlFormula, packet)

    myresult = mycursor.fetchall()

    print(myresult)


mysql_server = input("MySQL Server address: ")

mydb = mysql.connector.connect(
    host=mysql_server,
    user="chatuser",
    passwd="chatpasswort",
    database="chat_datenbank"
)

print(mydb)

username = input("Bitte Nutzernamen eingeben: ")
print("Hallo " + username + "!")
passwort_überprüfen()

while True:
    modeinput = input("1: Nachrichten lesen, 2: Nachricht schreiben, 3: Nachrichten löschen ")

    try:
        mode = int(modeinput)
    except:
        mode = 4

    if mode == 1:
        nachrichten_auslesen()

    if mode == 2:
        print("")
        nachricht = input("Ihre Nachricht: ")
        mycursor = mydb.cursor()

        sqlFormula = "INSERT INTO chatroom1 (username, text) VALUES (%s, %s)"
        nachrichtpacket = (username, nachricht)

        mycursor.execute(sqlFormula, nachrichtpacket)

        mydb.commit()

        print("Nachricht gesendet: " + nachricht)
        print("")

    if mode == 3:
        nachrichten_auslesen()

        nachricht_nummer = input("Welche Nachricht? ")
        try:
            mycursor = mydb.cursor()

            sqlFormula = "DELETE FROM `chatroom1` WHERE `chatroom1`.`id` = %s"
            packet = (nachricht_nummer)

            mycursor.execute(sqlFormula, packet)

            mydb.commit()
        except:
            print("Fehler beim Löschen!")

    if mode > 3:
        print("Bitte gültige Zahl eingeben!")