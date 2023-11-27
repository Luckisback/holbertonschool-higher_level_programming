#!/usr/bin/python3

""" A script that lists all states with a name starting with upper 'N'  """

import MySQLdb
import sys

if __name__ == "__main__":

    u = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    con = MySQLdb.connect(user=u, password=pwd,
                                 database=db, host="localhost",
                                 port=3306)

    cur = con.cursor()
    req = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id"
    cur.execute(req)

    res_tup = cur.fetchall()

    for eta in res_tup:
        print(eta)

    cursor.close()
    con.close()
