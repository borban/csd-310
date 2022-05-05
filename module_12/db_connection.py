import mysql.connector
from mysql.connector import errorcode


def create_session():
    config = {
        "user" : "whatabook_user",
        "password" : "MySQL8IsGreat!",
        "host" : "127.0.0.1",
        "database" : "whatabook",
        "raise_on_warnings" : True
    }

    try:
        db = mysql.connector.connect(**config)
        return db
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(" The supplied username or password are invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(" The specified datbase does not exist")
        else:
            print(err)