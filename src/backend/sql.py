import json
import os
import MySQLdb
 
MYSQL_HOST = "tax_stopper_db"
MYSQL_DATABASE = os.environ['MYSQL_DATABASE']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
MYSQL_TABLE = "paycheck"

class modelPay:
    def connect(self):
        return MySQLdb.connect(
            host = MYSQL_HOST,
            user = MYSQL_USER,
            passwd = MYSQL_PASSWORD,
            db = MYSQL_DATABASE
        )

    def getAll(self):
        connection = self.connect()
        with connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
            sql = f"SELECT * FROM {MYSQL_TABLE}"
            cursor.execute(sql)
            result = cursor.fetchall()
        return result if result else {}

    def register(self, year, month, income1 = 0, income2 = 0):
        connection = self.connect()
        with connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
            sql = f"INSERT INTO {MYSQL_TABLE} values({year}, {month}, {income1}, {income2})"
            cursor.execute(sql)
            connection.commit()
    
    def update(self, year, month, income1, income2):
        connection = self.connect()
        with connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
            sql = f"UPDATE {MYSQL_TABLE} SET income1 = {income1}, income2 = {income2} "
            sql += f"WHERE year = {year} AND month = {month}"
            cursor.execute(sql)
            connection.commit()
    
    def delete(self, year, month):
        connection = self.connect()
        with connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
            sql = f"DELETE FROM {MYSQL_TABLE} WHERE year = {year} AND month = {month}"
            cursor.execute(sql)
            connection.commit()