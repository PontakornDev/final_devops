import MySQLdb
from nameko.rpc import rpc


def connect():
    DBconnect = MySQLdb.connect(host='db',
                                user='devops',
                                passwd='devops101',
                                db='devops_db',
                                port=3306)
    return DBconnect


def query(username, password):
    DBconnect = connect()
    cur = DBconnect.cursor()
    cur.execute("SELECT * FROM userdata30 WHERE username=(%s) AND password=(%s);",
                (username, password))
    DBconnect.commit()
    DBconnect.close()


class Service:
    name = "userlogin"

    @rpc
    def query(self, username, password):
        result = query(username, password)
        return result
