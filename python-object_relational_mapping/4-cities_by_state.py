#!/usr/bin/python3

""" A script that lists all cities from the database """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    h = "localhost"
    p = 3306
    u = argv[1]
    mdp = argv[2]
    bdd = argv[3]

    con = MySQLdb.connect(host=h, port=p, user=u, password=mdp, database=bdd)
    cur = con.cursor()
    cur.execute("SELECT cities.id, cities.name,\
                states.name FROM cities JOIN states\
                    ON states.id = cities.state_id ORDER BY cities.id ASC")
    res = cur.fetchall()

    for _ in res:
        print(_)

    cur.close()
    con.close()
