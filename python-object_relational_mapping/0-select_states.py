#!/usr/bin/python3

""" A script that lists all states from database """

import MySQLdb

if __name__ == "__main__":

    con = MySQLdb.connect(host='localhost', port=3306, user='root', password='', database='hbtn_0e_0_usa')
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    result = cur.fetchall()
    for _ in result:
        print(_)
    cur.close()
    con.close()
