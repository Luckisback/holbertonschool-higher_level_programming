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
    u = "root"
    mps = ""
    dtb = "hbtn_0e_0_usa"

    """ Connection to the data base """
    con = MySQLdb.connect(port=p, database=dtb, user=u, host=h, password=mps)
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    res = cur.fetchall()

    """ Comparaison and displaying matched values """
    index_val = len(argv) -1
    for _ in res:
        if _[1] == argv[index_val]:
            print(_)

    """ Closing the connection """
    cur.close()
    con.close()
