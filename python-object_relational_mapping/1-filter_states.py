#!/usr/bin/python3

import MySQLdb
import sys

""" A script that lists all states with a name starting with upper 'N'  """

if __name__ == "__main__":

    """ Declaration of connection's parameters """
    h = "localhost"
    p = 3306
    u = argv[1]
    pwd = argv[2]
    db = argv[3]

    """ Connection to the database """
    con = MySQLdb.connect(host=h, port=p, user=u, password=pwd, database=db)
    cur = con.cursor()

    """ Recovering information from a table """
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")

    """ Displaying the retrieved contant """
    result = cur.fetchall()

    for _ in result:
        print(_)

    """ Closing database's connection """
    cur.close()
    con.close()
