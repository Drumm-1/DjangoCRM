


import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'pass123'
)
cursorObjet = dataBase.cursor()

cursorObjet.execute("CREATE DATABASE elderco")

print("All done")
