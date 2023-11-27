#!/usr/bin/python3

""" A script that lists all states from database """

import MySQLdb

if __name__ == "__main__":

    """connection to the dabtabase """
    con = MySQLdb.connect(host=localhost, port=3306, user="root", password="", database="hbtn_0e_0_usa")
    cur = con.cursor()

    """ The query for retieving information from the table """
    cur.execute("SELECT * FROM states ORDER BY states.id")

    """ Information recovery """
    result = cur.fetchall()

    """ listing information"""
    for _ in result:
        print(_)

    """ Closing the connection """
    cur.close()
    con.close()
