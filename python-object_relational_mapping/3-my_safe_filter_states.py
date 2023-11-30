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
    nom_stat = argv[4]

    con = MySQLdb.connect(host=h, port=p, user=u, password=mps, database=dtb)
    cur = con.cursor()
    q = "SELECT * FROM states WHERE name = '{}'\
        ORDER BY states.id".format(nom_stat,)
    cur.execute(q)

    res = cur.fetchall()

    for _ in res:
        print(_)

    cur.close()
    con.close()
