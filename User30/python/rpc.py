import MySQLdb
from nameko.rpc import rpc


def connect():
    DBconnect = MySQLdb.connect(host='db',
                                user='devops',
                                passwd='devops101',
                                db='devops_db',
                                port=3306)
    return DBconnect


def insert(username, password, email):
    DBconnect = connect()
    cur = DBconnect.cursor()
    cur.execute("INSERT INTO userdata30 (username, password, email) VALUES (%s, %s, %s);",
                (username, password, email))
    id = cur.lastrowid
    DBconnect.commit()
    DBconnect.close()
    return id


class Service:
    name = "user"

    @rpc
    def insert(self, username, password, email):
        result = insert(username, password, email)
        return result
