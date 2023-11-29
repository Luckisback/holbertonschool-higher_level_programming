#!/usr/bin/python3

""" A script that taks in arguments and displays all value in a table
    This code is safe from MySQL injection
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    h = "localhost"
    p = 3306
    u = argv[1]
    mps = argv[2]
    dtb = argv[3]
    nom_stat = argv[len(argv) - 1]

    con_val = """port = %s, database = %s, user = %s,
    host = %s, password = %s""" % (h, p, u, mps, dtb)
    con = MySQLdb.connect(con_val)
    cur = con.cursor()
    qry = "SELECT * FROM states WHERE name = %s ORDER BY states.id"
    cur = (qry, nom_stat)

    res = cur.fetchall()

    for _ in res:
        if _[1] == argv[nom_stat]:
            print(_)

    cur.close()
    con.close()
