#!/usr/bin/python3

import MySQLdb
import sys

""" A script that lists all states with a name starting with upper 'N'  """

if __name__ == "__main__":

    h = "localhost"
    p = 3306
    u = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    con = MySQLdb.connect(host=h, port=p, user=u, password=pwd, database=db)
    cur = con.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id")

    result = cur.fetchall()

    for eta in result:
        if sta[1][0] == "N":
            print(eta)

    cur.close()
    con.close()
