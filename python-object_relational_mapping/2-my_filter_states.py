#!/usr/bin/python3

""" A script that compares a argumaent with a table's value """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    """ Declaration for connction to the database """
    h="localhost"
    p=3306
    u=sys.argv[1]
    pwd=argv[2]
    db=argv[3]

    """ Connection to the database """
    con = MySQLdb.connect(host=h, port=p, user=u, password=pwd, database=db)
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    q_result = cur.fetchall()

    """ Searshing for a matched value """
    index_arg = len(argv) - 1
    for _ in q_result:
        if _[1] == argv[index_arg]:
            print(_)

    """ Closing the connexion """
    cur.close()
    con.close()
