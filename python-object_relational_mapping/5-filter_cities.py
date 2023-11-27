#!/usr/bin/python3

""" a script that takes in the name of a state as an argument
    and lists all cities of that state 
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    """ Declaration of the connection's parameters """
    h = "localhost"
    p = 3306
    u = "root"
    mdp = ""
    bdd = "hbtn_0e_4_usa"

    """ Connection to the database """
    con = MySQLdb.connect(host=h, port=p, user=u, password=mdp, database=bdd)
    cur = con.cursor()
    cur.execute("SELECT cities.name, states.name FROM cities JOIN states ON states.id = cities.state_id ORDER BY cities.id")
    res = cur.fetchall()

    """ Compararing and displaying the selected rows """
    index_arg = len(argv) -1
    disp_list = []
    for _ in res:
        if _[1] == argv[index_arg]:
            disp_list.append("{}".format(_[0]))
    print(", ".join(disp_list))

    """ Closing connection """
    cur.close()
    con.close()

    """ """
