import json
import os
import MySQLdb
 
MYSQL_HOST = "tax_stopper_db"
MYSQL_DATABASE = os.environ['MYSQL_DATABASE']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
MYSQL_TABLE = "paycheck"

class modelPay:
    def __init__(self):
        self.connection = self.connect()

    def connect(self):
        return MySQLdb.connect(
            host = MYSQL_HOST,
            user = MYSQL_USER,
            passwd = MYSQL_PASSWORD,
            db = MYSQL_DATABASE
        )

    
    def close(self):
        if self.cursor: self.cursor.close()
    
    def getAll(self):
        with self.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
            sql = f"SELECT * FROM {MYSQL_TABLE}"
            cursor.execute(sql)
            result = cursor.fetchall()
        return result if result else {}

    def register(self, year, month, income1 = 0, income2 = 0):
        with self.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
            sql = f"insert into paycheck values('{str(year)}', '{str(month)}', {str(income1)}, {str(income2)})"
            cursor.execute(sql)
            self.connection.commit()