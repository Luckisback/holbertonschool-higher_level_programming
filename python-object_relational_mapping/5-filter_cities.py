#!/usr/bin/python3

""" a script that takes in the name of a state as an argument
    and lists all cities of that state 
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    h = "localhost"
    p = 3306
    u = argv[1]
    mdp = argv[2]
    bdd = argv[3]
    nom_stat = argv[len(argv) -1]

    """ Connection to the database """
    con = MySQLdb.connect(host=h, port=p, user=u, password=mdp, database=bdd)
    cur = con.cursor()
    cur.execute("SELECT cities.name, states.name FROM cities JOIN states ON states.id = cities.state_id ORDER BY cities.id")
    res = cur.fetchall()
    disp_list = []

    for _ in res:
        if _[1] == nom_stat:
            disp_list.append("{}".format(_[0]))
    print(", ".join(disp_list))

    cur.close()
    con.close()
