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

    param_con = "port = '%s',\
        database = '%s', user= '%s',\
            host = '%s', password = '%s'" % (p, dtb, u, h, mps)
    con = MySQLdb.connect(param_con)
    cur = con.cursor()
    q = "SELECT * FROM states WHERE name = '{}'\
    AND name LIKE BINARY 'N%' ORDER BY states.id"
    cur.execute(q)

    res = cur.fetchall()

    for _ in res:
        print(_)

    cur.close()
    con.close()
