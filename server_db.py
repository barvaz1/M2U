import sqlite3
from sqlite3 import Error

db_file = r"Users.db"


class Controller_db:
    def __init__(self):

        # create a database connection to a SQLite database
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)

        print(self.conn)

    def create_user_tabel(self):
        try:
            c = self.conn.cursor()
            c.execute(""" CREATE TABLE IF NOT EXISTS USERS (
                            "usrName"	TEXT NOT NULL UNIQUE, 
                            "usrEmail"	TEXT NOT NULL UNIQUE,
                            "usrPWD"	TEXT NOT NULL,
                            PRIMARY KEY("usrName")
                                ); """)
        except Error as e:
            print(e)

    def create_user(self, name, email, password):
        print(self.conn)
        sql = """ INSERT INTO USERS (
                          usrName,
                          usrEmail,
                          usrPWD
                      )
                      VALUES (
                          '{}',
                          '{}',
                          '{}'
                          ); """

        sql = sql.format(name, email, password)

        print(sql)
        cur = self.conn.cursor()

        count = cur.execute(sql)
        self.conn.commit()

        cur.close()
        return

    def user_sing_up(self, data):
        data["success"] = False
        if self.check_if_user_name_exists(data["user name"]):
            data["user name"] = "user name exists"

        elif self.check_if_email_exists(data['E-mail']):
            data['E-mail'] = "Email exists"

        else:
            try:
                self.create_user(data["user name"], data['E-mail'], data["password"])
                data["success"] = True
            except:
                pass

        return data


        print("heyheyhey")
        print(data)
        return data

    def check_if_user_name_exists(self, user_name):
        # check if the user name existsin the data base

        sql = """SELECT usrName FROM USERS WHERE usrName = '{}' LIMIT 1"""
        sql = sql.format(user_name)
        cur = self.conn.cursor()

        if cur.execute(sql).fetchall():
            return True
        else:
            return False

    def check_if_email_exists(self, user_name):
        # check if the user name existsin the data base

        sql = """SELECT usrEmail FROM USERS WHERE usrEmail = '{}' LIMIT 1"""
        sql = sql.format(user_name)
        cur = self.conn.cursor()

        if cur.execute(sql).fetchall():
            return True
        else:
            return False


if __name__ == '__main__':
    x = Controller_db()
    x.create_user_tabel()
    print(x.user_sing_up({"user name": "moshe2",
                          "user Email": "moshe@gmail.com2"}))
