#!/usr/bin/python3

""" A script that lists all cities from the database """

import MySQLdb

if __name__ == "__main__":

    """ Declaration of connection's parameters """
    h = "localhost"
    p = 3306
    u = "root"
    mdp = ""
    bdd = "hbtn_0e_4_usa"

    """ Connection to the database """
    con = MySQLdb.connect(host=h, port=p, user=u, password=mdp, database=bdd)
    cur = con.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC")
    res = cur.fetchall()

    """ Displaying the selection """
    for _ in res:
        print(_)

    """ Closing the connection """
    cur.close()
    con.close()
