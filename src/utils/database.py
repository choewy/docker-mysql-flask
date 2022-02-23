import pymysql


class Database:
    def __init__(self):
        self.conn = pymysql.connect(host="localhost",
                                    port=33061,
                                    user="root",
                                    password="root",
                                    db="app")
        self.curs = self.conn.cursor()


db = Database()
