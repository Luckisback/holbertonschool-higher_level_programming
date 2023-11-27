#!/usr/bin/python3

""" A script that lists all states from database """

import MySQLdb
import sys

if __name__ == "__main__":

    h = "localhost"
    p = 3306
    u = sys.argv[1]
    mdp = sys.argv[2]
    bdd = sys.argv[3]

    con = MySQLdb.connect(host=h, port=p, user=u, password=mdp, database=bdd)
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    result = cur.fetchall()

    for _ in result:
        print(_)

    cur.close()
    con.close()
