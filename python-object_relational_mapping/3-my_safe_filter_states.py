#!/usr/bin/python3

""" A script that taks in arguments and displays all value in a table
    This code is safe from MySQL injection
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    """ Declaration of connextion's parameters """
    h ="localhost"
    p = 3306
    u = argv[1]
    mps = argv[2]
    dtb = arg[3]
    nom_stat = argv[4]

    """ Connection to the data base """
    con = MySQLdb.connect(port=p, database=dtb, user=u, host=h, password=mps)
    cur = con.cursor()
    qry = "SELECT * FROM states WHERE name = %s ORDER BY states.id"
    cur = (qry, (nom_stat,))

    res = cur.fetchall()

    """ Comparaison and displaying matched values """
    index_val = len(argv) -1
    for _ in res:
        if _[1] == argv[index_val]:
            print(_)

    """ Closing the connection """
    cur.close()
    con.close()
