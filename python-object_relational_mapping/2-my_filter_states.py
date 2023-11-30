#!/usr/bin/python3

""" A script that compares a argumaent with a table's value """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    """ Declaration for connction to the database """
    h = "localhost"
    p = 3306
    u = argv[1]
    pwd = argv[2]
    db = argv[3]
    nom_stat = argv[len(argv) - 1]

    """ Connection to the database """
    con = MySQLdb.connect(host=h,
                          port=p, user=u,
                          password=pwd,
                          database=db)
    cur = con.cursor()
    Qry = "SELECT * FROM states\
        WHERE name = BINARY %s ORDER BY states.id".format(nom_stat)
    cur.execute(Qry)
    q_result = cur.fetchall()

    for _ in q_result:
        print(_)

    cur.close()
    con.close()
