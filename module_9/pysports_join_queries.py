# Ben Orban
# Assignment 9.2 Pysports Basic table joins

import mysql.connector
from mysql.connector import errorcode

config = {
    "user" : "pysports_user",
    "password" : "MySQL8IsGreat!",
    "host" : "127.0.0.1",
    "database" : "pysports",
    "raise_on_warnings" : True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player p INNER JOIN team t ON p.team_id = t.team_id")
    players = cursor.fetchall()

    print("--DISPLAYING PLAYER RECORDS--")
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}\n".format(player[3]))
        
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified datbase does not exist")
    else:
        print(err)
finally:
    db.close()