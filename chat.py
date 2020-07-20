import mysql.connector

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

while True:
    modeinput = input("1: Nachrichten lesen, 2: Nachricht schreiben, 3: Nachrichten löschen ")

    try:
        mode = int(modeinput)
    except:
        mode = 10

    if mode == 1:
        #Nachrichten auslesen und anzeigen
        print("Aktuelle Nachrichten: ")
        print("")

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM chatroom1")

        myresult = mycursor.fetchall()
        
        for row in myresult:
            print("(" + str(row[0]) + ") " + row[1] + ": " + row[2])

        print("")

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
        #Nachrichten auslesen und anzeigen
        print("Aktuelle Nachrichten: ")
        print("")

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM chatroom1")

        myresult = mycursor.fetchall()
        
        for row in myresult:
            print("(" + str(row[0]) + ") " + row[1] + ": " + row[2])

        print("")

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