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

    def check_user(self, name, email, password):
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




if __name__ == '__main__':
    x = Controller_db()
    x.create_user_tabel()
    x.create_user('try1', 'try@try.com1', '1234try')
